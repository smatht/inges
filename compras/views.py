import datetime

import xlwt
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from xlrd import open_workbook
from xlutils.copy import copy

from sistema_inges import settings
from .serializers import CompraSerializer
from .models import Compra

class ComprasViewSet(viewsets.ModelViewSet):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer


ARRAY_MESES = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']


@login_required
@csrf_exempt
def InformeAnalisisCorporativo(request):
    now = datetime.datetime.now()
    mes = now.month
    template = 'analisis_corporativo.html'
    if request.method == "GET":
        if request.GET.get('fecha'):
            mes = request.GET.get('fecha')[-2:]
            # anio = int(request.POST.get('anio'))
            # now = datetime.datetime(anio,mes,1)

    if request.method == "POST":
        if request.POST.get('fecha'):
            mes = request.GET.get('fecha')[-2:]
        compras = Compra.objects.filter(fContabilizar__month=mes)
        xlwt.add_palette_colour("color_neto", 0x21)
        xlwt.add_palette_colour("color_iva", 0x22)
        xlwt.add_palette_colour("color_percepciones", 0x23)
        xlwt.add_palette_colour("color_total", 0x24)

        estilo_general = xlwt.easyxf(
            'font: name Arial, colour black, bold off; align: wrap on, vert centre, horiz center')
        estilo_empresa = xlwt.easyxf('font: name Arial, colour black, bold off; align: wrap on, horiz left')
        estilo_fecha = xlwt.easyxf('', num_format_str='DD-MMM-YY')
        estilo_moneda = xlwt.easyxf(
            'font: name Arial, colour black, bold off; align: wrap on, vert centre, horiz center',
            num_format_str='$#,##0.00')
        borders = xlwt.Borders()
        borders.left = 2
        borders.right = 2
        borders.top = 1
        borders.bottom = 1
        estilo_general.borders = borders
        estilo_empresa.borders = borders
        estilo_fecha.borders = borders
        estilo_moneda.borders = borders
        # wb = xlwt.Workbook()
        # ws = wb.add_sheet('FACTURAS',cell_overwrite_ok=True)
        # i = 3
        # for fr in facturas_recibidas:
        #     ws.write(i, 2, fr.fecha, style1)
        #     # ws.write(i, 3, fr.emisor, style1)
        #     ws.write(i, 4, fr.nro_factura, style0)
        #     ws.write(i, 5, fr.total(), style0)
        #     i = i + 1
        # ws.write(0, 0, 'Test', style0)
        # ws.write(1, 0, datetime.datetime.now(), style1)
        # ws.write(2, 0, 4)
        # ws.write(2, 1, 1)
        # ws.write(2, 2, xlwt.Formula("A3+B3"))
        rb = open_workbook("sistema_inges/" + settings.STATIC_URL + '/xls/plantilla/plantilla.xls',
                           formatting_info=True)
        wb = copy(rb)
        wb.set_colour_RGB(0x22, 41, 117, 217)
        wb.set_colour_RGB(0x21, 242, 221, 64)
        wb.set_colour_RGB(0x23, 115, 76, 65)
        wb.set_colour_RGB(0x24, 56, 166, 62)

        estilo_neto = xlwt.easyxf(
            'font: name Arial, bold on; align: wrap on, vert centre, horiz center; pattern: pattern solid, fore_colour color_neto')  # 11 * 20, for 11 point
        estilo_iva = xlwt.easyxf(
            'font: name Arial, bold on; align: wrap on, vert centre, horiz center; pattern: pattern solid, fore_colour color_iva')
        estilo_percepciones = xlwt.easyxf(
            'font: name Arial, bold on, height 180; align: wrap on, vert centre, horiz center; pattern: pattern solid, fore_colour color_percepciones')
        estilo_total = xlwt.easyxf(
            'font: name Arial, bold on; align: wrap on, vert centre, horiz center; pattern: pattern solid, fore_colour color_total')
        bordersTit = xlwt.Borders()
        bordersTit.left = 2
        bordersTit.right = 2
        bordersTit.top = 2
        bordersTit.bottom = 2
        estilo_neto.borders = bordersTit
        estilo_iva.borders = bordersTit
        estilo_percepciones.borders = bordersTit
        estilo_total.borders = bordersTit

        ws = wb.get_sheet(0)

        ws.write(2, 4, "SUBTOTAL (NETO)", estilo_neto)
        ws.write(2, 5, "IVA", estilo_iva)
        ws.write(2, 6, "PERCEPCIONES OTROS", estilo_percepciones)
        ws.write(2, 7, "TOTAL", estilo_total)

        ws.write(0, 3, ARRAY_MESES[mes] + ' ' + now.strftime("%Y"), estilo_general)

        i = 3
        for compra in compras:
            ws.write(i, 1, compra.fDocumento, estilo_fecha)
            ws.write(i, 2, compra.proveedor.__unicode__(), estilo_empresa)
            ws.write(i, 3, compra.NumeroIdentificacion(), estilo_general)
            ws.write(i, 4, compra.totBruto, estilo_moneda)
            ws.write(i, 5, compra.totImpuestos, estilo_moneda)
            ws.write(i, 6, 0, estilo_moneda)
            ws.write(i, 7, compra.totNeto, estilo_moneda)
            i = i + 1

        estilo_neto = xlwt.easyxf(
            'font: name Arial, bold on; align: wrap on, vert centre, horiz center; pattern: pattern solid, fore_colour color_neto',
            num_format_str='$#,##0.00')  # 11 * 20, for 11 point
        estilo_iva = xlwt.easyxf(
            'font: name Arial, bold on; align: wrap on, vert centre, horiz center; pattern: pattern solid, fore_colour color_iva',
            num_format_str='$#,##0.00')
        estilo_percepciones = xlwt.easyxf(
            'font: name Arial, bold on; align: wrap on, vert centre, horiz center; pattern: pattern solid, fore_colour color_percepciones',
            num_format_str='$#,##0.00')
        estilo_total = xlwt.easyxf(
            'font: name Arial, bold on; align: wrap on, vert centre, horiz center; pattern: pattern solid, fore_colour color_total',
            num_format_str='$#,##0.00')
        ws.write(106, 4, xlwt.Formula("SUM(E4:E105)"), estilo_neto)
        ws.write(106, 5, xlwt.Formula("SUM(F4:F105)"), estilo_iva)
        ws.write(106, 6, xlwt.Formula("SUM(G4:G105)"), estilo_percepciones)
        ws.write(106, 7, xlwt.Formula("SUM(H4:H105)"), estilo_total)

        fechaXLS = "AnalisisCorporativo_" + str(now.day) + "-" + str(now.month) + "-" + str(now.year) + ".xls"
        wb.save("sistema_inges/" + settings.STATIC_URL + '/xls/' + fechaXLS)
        return HttpResponseRedirect(settings.STATIC_URL + '/xls/' + fechaXLS)

    # facturas_emitidas = Emision_factura.objects.filter(fecha_registro__month=mes)
    compras = Compra.objects.filter(fContabilizar__month=mes)
    facturacion_iva = 0
    descuento_iva = 12000
    total_ingresos = 0
    subtotal_ingresos = 0
    f_r_civa = 0
    f_r_siva = 0
    percep_otros = 0
    totalAlb = 0
    # for f in facturas_emitidas:
    #     descuento_iva = descuento_iva + f.impuesto()
    #     total_ingresos = total_ingresos + f.total()
    #     subtotal_ingresos = subtotal_ingresos + (total_ingresos - descuento_iva)
    for compra in compras:
        facturacion_iva = facturacion_iva + compra.totImpuestos
        f_r_civa = f_r_civa + compra.totNeto
        f_r_siva = f_r_siva + compra.totBruto
        # percep_otros = percep_otros + fr.percepciones_otros
    # for ar in albaranes_recibidos:
    #     totalAlb = totalAlb + ar.total

    gasto_c_iva = f_r_civa + totalAlb
    gasto_s_iva = f_r_siva + totalAlb

    return render(request, template, {'request': request, 'fact_iva': facturacion_iva,
                                      'title': 'Informes', 'desc_iva': descuento_iva, 'gastoCIva': gasto_c_iva,
                                      'gastoSIva': gasto_s_iva, 'mespy': mes, 'detalleFacturasR': compras,
                                      # 'detalleFacturasE': facturas_emitidas,
                                      # 'detalleAlbaranesR': albaranes_recibidos,
                                      'percep_otros': percep_otros, 'totalAlb': totalAlb,
                                      'total_ingresos': total_ingresos,
                                      'subtotal_ingresos': subtotal_ingresos, 'f_r_civa': f_r_civa,
                                      'f_r_siva': f_r_siva}, context_instance=RequestContext(request))


