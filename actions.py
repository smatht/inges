# -*- coding: utf-8 -*-
# taken from http://weitlandt.com/theme/2010/05/wir-djangonauten-csv-export-nach-excel-mit-umlauten/
# + mucho amor de @julian_amaya y @votaguz

import csv
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.template import Context, Template
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas
from io import BytesIO

from reportlab.platypus import Table
from reportlab.platypus import TableStyle


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


def tabla(pdf, y, qs):
    # Creamos una tupla de encabezados para neustra tabla
    encabezados = ('fecha', 'Proveedor', 'Autorizado', 'Destino', 'Remitente')
    # Creamos una lista de tuplas que van a contener a las personas
    detalles = [(qs.fecha, qs.proveedor, qs.se_autoriza, qs.destino, qs.remitente)]
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
    detalle_orden.drawOn(pdf, 60, y)


def export_OR_as_pdf(modeladmin, request, queryset):
    if not request.user.is_staff:
        raise PermissionDenied
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'
    buffer = BytesIO()
    n = str(queryset[0].id)
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
    tabla(p, y, queryset[0])
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
