# encoding: utf-8
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied, ObjectDoesNotExist
from django.http import HttpResponse
from django.template import Context, Template
from reportlab.lib import colors
from reportlab.lib.units import cm, inch
from reportlab.pdfgen import canvas
from io import BytesIO

from reportlab.platypus import Frame, Spacer
from reportlab.platypus import Table
from reportlab.platypus import TableStyle
from reportlab.platypus.para import Paragraph
from reportlab.lib.styles import getSampleStyleSheet

from fondos.moneda import Moneda
from mantenimiento.models import ExtendUser

stylesheet=getSampleStyleSheet()
#Definimos margenes
margXizq = 30
margYtop = 800
importe = 0

def orden_pago_as_pdf(request, obj):
    global importe
    if not request.user.is_staff:
        raise PermissionDenied

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="somefilename.pdf"'
    buffer = BytesIO()
    n = str(obj.id)
    # Creacion objeto PDF
    p = canvas.Canvas(buffer)

    # Imprimimos nombre de la empresa
    p.drawString(margXizq, margYtop, obj.empresa.__str__())
    p.setFont("Helvetica", 11)
    p.drawString(margXizq*14, margYtop, obj.fCarga.strftime('%d-%m-%Y %I:%M %p'))

    # Dibujamos la cabecera
    importe = Moneda(obj.importe)
    frameCabecera(p, obj)

    # Dibujamos Cuerpo
    frameCuerpo(p, obj)

    # Dibujamos Cuerpo
    frameTotales(p, obj)

    # Dibujamos Pie
    framePie(p, obj)

    # Cierra PDF, y terminamos.
    p.showPage()
    p.save()
    p = buffer.getvalue()
    buffer.close()
    response.write(p)
    return response

def frameCabecera(pdf, obj):
    beneficiario = obj.beneficiario()
    if type(beneficiario) is User:
        strBeneficiario = beneficiario.first_name + ', ' + beneficiario.last_name
    else:
        strBeneficiario = beneficiario.__str__()
    motivo = obj.motivo.__str__()
    if getattr(obj.beneficiario(), 'cuit', None) is None:
        usr = ExtendUser.objects.get(pk=obj.beneficiario().pk)
        cdn = str(usr.dni)
    else:
        cdn = str(obj.beneficiario().cuit)
    # Recuadro
    pdf.setStrokeColorRGB(0, 0, 0)
    f = Frame(margXizq, margYtop-185, 540, 170)
    f.drawBoundary(pdf)
    # titulo
    pdf.setFont("Helvetica-Bold", 13)
    pdf.drawString(margXizq*7, margYtop-45, u"ORDEN DE PAGO Nº ")
    pdf.drawString(margXizq*11+12, margYtop-45, str(obj.id).zfill(5))
    # Tabla Cabecera
    p0 = Paragraph('''<b>Beneficiario:</b>''', stylesheet['Normal'])
    p1 = Paragraph('''<b>Cuit/DNI:</b>''', stylesheet['Normal'])
    p2 = Paragraph('''<b>Recibo:</b>''', stylesheet['Normal'])
    p3 = Paragraph('''<b>Motivo:</b>''', stylesheet['Normal'])
    data = [[p0, strBeneficiario], [p1, cdn], [p2, ' '], [p3, motivo]]
    t1 = Table(data, colWidths=[3 * cm, 5 * cm])
    t1.setStyle(TableStyle(
        [
            # La primera fila(encabezados) va a estar centrada
            # ('ALIGN', (0, 0), (3, 0), 'CENTER'),
            # Los bordes de todas las celdas serán de color negro y con un grosor de 1
            ('LINEBELOW', (1, 0), (1, 3),  1, colors.black),
            # El tamaño de las letras de cada una de las celdas será de 10
            # ('FONTSIZE', (0, 0), (-1, -1), 10),
        ]
    ))

    pdf.rect(margXizq, margYtop-145, 540, 1, 1, 1)

    p4 = Paragraph('''<b>SON PESOS: </b>''', stylesheet['Normal'])
    data2 = [[p4, importe.toText()]]
    t2 = Table(data2, colWidths=[3 * cm, 5 * cm])

    t1.wrapOn(pdf, 800, 600)
    t2.wrapOn(pdf, 800, 600)
    t1.drawOn(pdf, margXizq+15, margYtop-135)
    t2.drawOn(pdf, margXizq+15, margYtop-175)

def frameCuerpo(pdf, obj):
    # Recuadro
    pdf.setStrokeColorRGB(0, 0, 0)
    f = Frame(margXizq, margYtop-305, 540, 100)
    f.drawBoundary(pdf)

    pdf.setFont("Helvetica", 11)
    pdf.rect(margXizq, margYtop-225, 540, 0.5, 1, 1)
    pdf.setFont("Helvetica-Bold", 11)
    pdf.drawString(margXizq+6, margYtop-220, u"Concepto:")

    concepto = obj.comentario
    s = Spacer(0.2 * inch, 0.1 * inch)
    p = Paragraph(concepto, stylesheet["Normal"])
    data = [[p]]
    t = Table(data, colWidths=[500, 75])
    t.wrapOn(pdf, 800, 600)
    t.drawOn(pdf, margXizq + 10, margYtop - 280)

def frameTotales(pdf, obj):
    p0 = Paragraph('''<b>Valor entregado</b>''', stylesheet['Normal'])
    p1 = Paragraph('''<b>Importe</b>''', stylesheet['Normal'])
    p2 = Paragraph('''<b>''' + '$ {:,.2f}'.format(obj.importe) + '''</b>''', stylesheet['Normal'])
    data = [[p0, p1], ['Efectivo', p2]]
    t1 = Table(data, colWidths=[5 * cm, 3 * cm])
    t1.setStyle(TableStyle(
        [
            # La primera fila(encabezados) va a estar centrada
            # ('ALIGN', (0, 0), (3, 0), 'CENTER'),
            # Los bordes de todas las celdas serán de color negro y con un grosor de 1
            ('LINEBELOW', (0, 0), (1, 0), 1, colors.black),
            # El tamaño de las letras de cada una de las celdas será de 10
            # ('FONTSIZE', (0, 0), (-1, -1), 10),
        ]
    ))
    t1.wrapOn(pdf, 800, 600)
    t1.drawOn(pdf, margXizq*11, margYtop - 380)

def framePie(pdf, obj):
    # Recuadro controlado
    pdf.setStrokeColorRGB(0, 0, 0)
    f = Frame(margXizq, margYtop - 700, 230, 80)
    f.drawBoundary(pdf)

    pdf.setFont("Helvetica", 11)
    pdf.rect(margXizq, margYtop - 640, 230, 0.5, 1, 1)
    pdf.setFont("Helvetica-Bold", 11)
    pdf.drawString(margXizq + 6, margYtop - 635, u"Controlado")

    # Recuadro Recibido
    pdf.setStrokeColorRGB(0, 0, 0)
    f = Frame(margXizq, margYtop - 785, 230, 80)
    f.drawBoundary(pdf)

    pdf.setFont("Helvetica", 11)
    pdf.rect(margXizq, margYtop - 725, 230, 0.5, 1, 1)
    pdf.setFont("Helvetica-Bold", 11)
    pdf.drawString(margXizq + 6, margYtop - 720, u"Recibido")

    # Recuadro Autorizado
    pdf.setStrokeColorRGB(0, 0, 0)
    f = Frame(margXizq+240, margYtop - 700, 230, 80)
    f.drawBoundary(pdf)

    pdf.setFont("Helvetica", 11)
    pdf.rect(margXizq+240, margYtop - 640, 230, 0.5, 1, 1)
    pdf.setFont("Helvetica-Bold", 11)
    pdf.drawString(margXizq + 246, margYtop - 635, u"Autorizado")