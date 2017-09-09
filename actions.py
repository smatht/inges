# encoding: utf-8
# taken from http://weitlandt.com/theme/2010/05/wir-djangonauten-csv-export-nach-excel-mit-umlauten/

import csv

from django.core.exceptions import PermissionDenied, ObjectDoesNotExist
from django.http import HttpResponse
from django.template import Context, Template
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas
from io import BytesIO

from reportlab.platypus import Frame
from reportlab.platypus import Table
from reportlab.platypus import TableStyle
from reportlab.platypus.para import Paragraph
from reportlab.lib.styles import getSampleStyleSheet

from compras.models import PedidoItem, PedidoItemConcepto

stylesheet=getSampleStyleSheet()

def get_csv_from_dict_list(field_list, data):
    csv_line = ";".join(['{{ row.%s|addslashes }}' % field for field in field_list])
    template = "{% for row in data %}" + csv_line + "\n{% endfor %}"
    return Template(template).render(Context({"data": data}))


def export_as_csv(modeladmin, request, queryset):
    if not request.user.is_staff:
        raise PermissionDenied

    replace_dc = {'\n': '* ', '\r': '', ';': ',', '\"': '|', '\'': '|', 'True': 'Si', 'False': 'No'}
    opts = modeladmin.model._meta
    response = HttpResponse(content_type='text/csv; charset=utf-8')
    response['Content-Disposition'] = 'attachment; filename=%s.csv' % unicode(opts).replace('.', '_')
    w = csv.writer(response, delimiter=';')
    # import pdb; pdb.set_trace()
    try:
        field_names = modeladmin.model.get_csv_fields()
        v_field_names = field_names
    except:
        field_names = [field.name for field in opts.fields]
        v_field_names = [getattr(field, 'verbose_name') or field.name for field in opts.fields]
    # print field_names
    v_field_names = map(lambda x: x.encode('utf-8') if x != 'ID' else 'Id', v_field_names)

    w.writerow(v_field_names)
    ax = []
    for obj in queryset:
        acc = {}
        for field in field_names:
            try:
                uf = unicode(getattr(obj, field)()).encode('utf-8')
            except:
                try:
                    uf = unicode(getattr(obj, field)).encode('utf-8')
                except:
                    uf = ''
            for i, j in replace_dc.iteritems():
                uf = uf.replace(i, j)
            if uf == 'None':
                uf = ''
            acc[field] = uf

        ax.append(acc)
    response.write(get_csv_from_dict_list(field_names, ax))
    return response


def tabla(pdf, qs):
    # Creamos una tupla de encabezados para neustra tabla
    encabezados = ('fecha', 'Proveedor', 'Autorizado', 'Destino', 'Remitente')
    # Creamos una lista de tuplas que van a contener a las personas
    detalles = [(qs.fechaPedido, qs.proveedor.cuit, qs.se_autoriza, qs.destino, qs.remitente)]
    # Establecemos el tamaño de cada una de las columnas de la tabla
    detalle_orden = Table([encabezados] + detalles, colWidths=[2 * cm, 5 * cm, 5 * cm, 5 * cm])
    # Aplicamos estilos a las celdas de la tabla
    detalle_orden.setStyle(TableStyle(
        [
            # La primera fila(encabezados) va a estar centrada
            ('ALIGN', (0, 0), (3, 0), 'CENTER'),
            # Los bordes de todas las celdas serán de color negro y con un grosor de 1
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            # El tamaño de las letras de cada una de las celdas será de 10
            ('FONTSIZE', (0, 0), (-1, -1), 10),
        ]
    ))
    # Establecemos el tamaño de la hoja que ocupará la tabla
    detalle_orden.wrapOn(pdf, 800, 600)
    # Definimos la coordenada donde se dibujará la tabla
    detalle_orden.drawOn(pdf, 10, 600)


def frameCabecera(pdf, qs):
  pdf.setStrokeColorRGB(0,0,0)
  f = Frame(10,500, 570, 150)
  fb = Frame(12, 502, 566, 146)
  f.drawBoundary(pdf)
  fb.drawBoundary(pdf)

  # Tabla proveedor y domicilio
  p0 = Paragraph('''<b>Senor(es):</b>''', stylesheet['Normal'])
  p1 = Paragraph('''<b>Domicilio:</b>''', stylesheet['Normal'])
  data = [[p0, qs.proveedor],[p1, qs.proveedor.domicilio_comercial]]
  t1 = Table(data, colWidths=[3 * cm, 5 * cm])
  t1.setStyle(TableStyle(
    [
      # La primera fila(encabezados) va a estar centrada
      # ('ALIGN', (0, 0), (3, 0), 'CENTER'),
      # Los bordes de todas las celdas serán de color negro y con un grosor de 1
      ('LINEBELOW', (1, 0), (1, 1), 1, colors.black),
      # El tamaño de las letras de cada una de las celdas será de 10
      # ('FONTSIZE', (0, 0), (-1, -1), 10),
    ]
  ))

  # Tabla telefono y localidad
  p0 = Paragraph('''<b>Telefono:</b>''', stylesheet['Normal'])
  p1 = Paragraph('''<b>Localidad:</b>''', stylesheet['Normal'])
  data = [[p0, qs.proveedor.telefono], [p1, qs.proveedor.localidad]]
  t2 = Table(data, colWidths=[3 * cm, 5 * cm])
  t2.setStyle(TableStyle(
    [
      # La primera fila(encabezados) va a estar centrada
      # ('ALIGN', (0, 0), (3, 0), 'CENTER'),
      # Los bordes de todas las celdas serán de color negro y con un grosor de 1
      ('LINEBELOW', (1, 0), (1, 1), 1, colors.black),
      # El tamaño de las letras de cada una de las celdas será de 10
      # ('FONTSIZE', (0, 0), (-1, -1), 10),
    ]
  ))

  # Tabla autorizado
  p0 = Paragraph('''<b>Se autoriza a:</b>''', stylesheet['Normal'])
  p1 = Paragraph('''<b>DNI:</b>''', stylesheet['Normal'])
  try:
      dni = qs.se_autoriza.extenduser.dni
  except (ObjectDoesNotExist, AttributeError):
      dni = ''
  try:
    data = [[p0, qs.se_autoriza.get_full_name()], [p1, dni]]
  except (ObjectDoesNotExist, AttributeError):
      data = [[p0, " "], [p1, dni]]
  t3 = Table(data, colWidths=[3 * cm, 5 * cm])
  t3.setStyle(TableStyle(
    [
      # La primera fila(encabezados) va a estar centrada
      # ('ALIGN', (0, 0), (3, 0), 'CENTER'),
      # Los bordes de todas las celdas serán de color negro y con un grosor de 1
      ('LINEBELOW', (1, 0), (1, 1), 1, colors.black),
      # El tamaño de las letras de cada una de las celdas será de 10
      # ('FONTSIZE', (0, 0), (-1, -1), 10),
    ]
  ))

  # Tabla obra
  p0 = Paragraph('''<b>Obra:</b>''', stylesheet['Normal'])
  p1 = Paragraph(''' ''', stylesheet['Normal'])
  data = [[p0, qs.destino], [p1, '']]
  t4 = Table(data, colWidths=[3 * cm, 5 * cm])
  t4.setStyle(TableStyle(
    [
      # La primera fila(encabezados) va a estar centrada
      # ('ALIGN', (0, 0), (3, 0), 'CENTER'),
      # Los bordes de todas las celdas serán de color negro y con un grosor de 1
      ('LINEBELOW', (1, 0), (1, 1), 1, colors.black),
      # El tamaño de las letras de cada una de las celdas será de 10
      # ('FONTSIZE', (0, 0), (-1, -1), 10),
    ]
  ))

  t1.wrapOn(pdf, 800, 600)
  t2.wrapOn(pdf, 800, 600)
  t3.wrapOn(pdf, 800, 600)
  t4.wrapOn(pdf, 800, 600)

  t1.drawOn(pdf, 20, 600)
  t2.drawOn(pdf, 320, 600)
  t3.drawOn(pdf, 20, 540)
  t4.drawOn(pdf, 320, 540)


def frameDetalle(pdf, idOrden):
  f = Frame(10,55, 570, 437)
  f.drawBoundary(pdf)

  encabezado = ('CANT.', 'MATERIAL')
  # Detalle de tabla con 20 renglones
  # Recorre PedidoItem (linea por producto)
  detalle = []
  for qs in PedidoItem.objects.filter(pedido=idOrden).order_by('pk'):
      descripcion = qs.producto.descripcion + ' ' + qs.sAclaracion
      if (len(descripcion) <= 102):
          detalle += [(qs.sCantidad +' '+ qs.unidades.descripcionCorta, descripcion)]
      else:
          detalle += [(qs.sCantidad +' '+ qs.unidades.descripcionCorta, descripcion[:102])]
          if (len(descripcion[102:240]) <= 102):
              detalle += [('', descripcion[102:240])]
          else:
              detalle += [('', descripcion[102:240])]
              detalle += [('', descripcion[240:300])]

  # Recorre PedidoItemConcepto (linea por concepto)
  for qs in PedidoItemConcepto.objects.filter(pedido=idOrden).order_by('pk'):
      descripcion = qs.sDescripcion
      if (len(descripcion) <= 102):
          detalle += [(qs.sCantidad +' '+ qs.unidades.descripcionCorta, descripcion)]
      else:
          detalle += [(qs.sCantidad +' '+ qs.unidades.descripcionCorta, descripcion[:102])]
          if (len(descripcion[102:240]) <= 102):
              detalle += [('', descripcion[102:240])]
          else:
              detalle += [('', descripcion[102:240])]
              detalle += [('', descripcion[240:300])]

  while len(detalle) < 23:
      detalle = detalle + [('', '')]
      detalle_orden = Table([encabezado] + detalle, colWidths=[2 * cm, 17.95 * cm])

      detalle_orden.setStyle(TableStyle(
          [
            # La primera fila(encabezados) va a estar centrada
            ('ALIGN', (0, 0), (1, 0), 'CENTER'),
            # Los bordes de todas las celdas serán de color negro y con un grosor de 1
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            # El tamaño de las letras de cada una de las celdas será de 10
            ('FONTSIZE', (0, 0), (-1, -1), 10),
          ]
      ))
  # Establecemos el tamaño de la hoja que ocupará la tabla
  detalle_orden.wrapOn(pdf, 800, 600)
  # Definimos la coordenada donde se dibujará la tabla
  detalle_orden.drawOn(pdf, 12, 57)


def framePie(pdf, autorizador):
  f = Frame(10, 10, 570, 40)
  f.drawBoundary(pdf)

  # Tabla autorizado
  p0 = Paragraph('''<b>Firma:</b>.......................''', stylesheet['Normal'])
  puntos = "..."
  p1 = Paragraph('''<b>Aclaracion: </b>'''+str(autorizador.get_full_name()), stylesheet['Normal'])
  p3 = Paragraph('''<b>OBSERVACIONES:</b>'''+puntos*55, stylesheet['Normal'])
  data = [[p0, p1], [p3]]
  t = Table(data, colWidths=[5 * cm, 14.95 * cm])
  t.setStyle(TableStyle(
    [
      # La primera fila(encabezados) va a estar centrada
      # ('ALIGN', (0, 0), (3, 0), 'CENTER'),
      # Los bordes de todas las celdas serán de color negro y con un grosor de 1
      ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
      ('SPAN', (0, 1), (1, 1)),
      # El tamaño de las letras de cada una de las celdas será de 10
      # ('FONTSIZE', (0, 0), (-1, -1), 10),
    ]
  ))
  t.wrapOn(pdf, 800, 600)
  t.drawOn(pdf, 12, 12)


def tablaFecha(pdf, f):
  t = Table([(f.day, f.month, f.year)], colWidths=[1.4 * cm, 1.4 * cm, 1.4 * cm])
  # Aplicamos estilos a las celdas de la tabla
  t.setStyle(TableStyle(
    [
      # La primera fila(encabezados) va a estar centrada
      ('ALIGN', (0, 0), (2, 0), 'CENTER'),
      # Los bordes de todas las celdas serán de color negro y con un grosor de 1
      ('GRID', (0, 0), (-1, -1), 1, colors.black),
      # El tamaño de las letras de cada una de las celdas será de 10
      ('FONTSIZE', (0, 0), (-1, -1), 10),
    ]
  ))
  # Establecemos el tamaño de la hoja que ocupará la tabla
  t.wrapOn(pdf, 800, 600)
  # Definimos la coordenada donde se dibujará la tabla
  t.drawOn(pdf, 450, 685)


def export_OR_as_pdf(modeladmin, request, obj):
  if not request.user.is_staff:
        raise PermissionDenied

  # det = OrdenRetiro_detalle.objects.get(orden_retiro=queryset[0].id)

  response = HttpResponse(content_type='application/pdf')
  response['Content-Disposition'] = 'filename="somefilename.pdf"'
  buffer = BytesIO()
  n = str(obj.id)
  # Creacion objeto PDF
  p = canvas.Canvas(buffer)

  # Colocacion imagen membrete
  # archivo_imagen = settings.MEDIA_ROOT + '/img/memIng.png'
  try:
      archivo_imagen = obj.registro.membrete.path
  except ValueError:
      archivo_imagen = ""
  if (archivo_imagen <> ""):
      p.drawImage(archivo_imagen, 30, 625, 500, 300, preserveAspectRatio=True)

  p.setStrokeColorRGB(0.2, 0.3, 0.5)
  p.setFillColorRGB(0.2, 0.3, 0.5)
  # p.setLineWidth(3)
  p.rect(0,715,842,2,1,1)
  # Establecemos el tamaño de letra en 16 y el tipo de letra Helvetica
  p.setFillColorRGB(0, 0, 0)
  p.setFont("Helvetica-Bold", 18)

  # Dibujamos una cadena en la ubicación X,Y especificada
  p.drawString(230, 685, u"ORDEN DE RETIRO")
  p.setFont("Helvetica", 14)
  p.drawString(265, 665, u"ORIGINAL Nº ")
  p.drawString(355, 665, n.zfill(5))

  # Draw things on the PDF. Here's where the PDF generation happens.
  # See the ReportLab documentation for the full list of functionality.
  f = obj.fechaPedido
  tablaFecha(p, f)
  frameCabecera(p, obj)
  frameDetalle(p, obj.id)
  framePie(p, obj.firmante)

  # Close the PDF object cleanly, and we're done.
  p.showPage()
  p.save()
  p = buffer.getvalue()
  buffer.close()
  response.write(p)
  return response


def save_then_pdf(request, queryset):
    if not request.user.is_staff:
        raise PermissionDenied
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'
    buffer = BytesIO()
    n = str(queryset.id)
    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(buffer)
    # Establecemos el tamaño de letra en 16 y el tipo de letra Helvetica
    p.setFont("Helvetica", 16)
    # Dibujamos una cadena en la ubicación X,Y especificada
    p.drawString(230, 790, u"ORDEN DE RETIRO")
    p.setFont("Helvetica", 14)
    p.drawString(265, 770, u"ORIGINAL N ")
    p.drawString(350, 770, n)
    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    y = 600
    tabla(p, y, queryset)
    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    p = buffer.getvalue()
    buffer.close()
    response.write(p)
    return response


export_as_csv.short_description = "Exportar como CSV"
export_OR_as_pdf.short_description = "Exportar Orden de retiro a PDF"
