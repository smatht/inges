# encoding: utf-8
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

stylesheet=getSampleStyleSheet()
#Definimos margenes
margXizq = 30
margYtop = 800

def orden_pago_as_pdf(request, obj):
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
    frameCabecera(p, obj)

    # Cierra PDF, y terminamos.
    p.showPage()
    p.save()
    p = buffer.getvalue()
    buffer.close()
    response.write(p)
    return response

def frameCabecera(pdf, obj):
    beneficiario = obj.beneficiario()
    motivo = obj.motivo.__str__()
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
    p1 = Paragraph('''<b>Cuit:</b>''', stylesheet['Normal'])
    p2 = Paragraph('''<b>Recibo:</b>''', stylesheet['Normal'])
    p3 = Paragraph('''<b>Motivo:</b>''', stylesheet['Normal'])
    data = [[p0, beneficiario], [p1, ' '], [p2, ' '], [p3, motivo]]
    t1 = Table(data, colWidths=[3 * cm, 5 * cm])
    t1.setStyle(TableStyle(
        [
            # La primera fila(encabezados) va a estar centrada
            # ('ALIGN', (0, 0), (3, 0), 'CENTER'),
            # Los bordes de todas las celdas serán de color negro y con un grosor de 1
            # ('LINEBELOW', (1, 0), (1, 1),  1, colors.black),
            # El tamaño de las letras de cada una de las celdas será de 10
            # ('FONTSIZE', (0, 0), (-1, -1), 10),
        ]
    ))
    t1.wrapOn(pdf, 800, 600)
    t1.drawOn(pdf, margXizq+15, margYtop-150)