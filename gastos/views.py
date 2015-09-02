from gastos.models import Factura_recibida, Iva, Empresa_Ente
from django.shortcuts import render_to_response, get_object_or_404, HttpResponse, render, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from models import *
import datetime
import calendar
from gastos.forms import *
from django.template.context import RequestContext
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
# Para modificacion de hoja Excel
from xlrd import open_workbook
import xlwt
from xlutils.copy import copy

ARRAY_MESES = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']

def inicio(request):
    return HttpResponseRedirect("/administracion/")
    # template = 'inicio.html'
    # # return render(request, template,{"request":request})
    # username = password = ''
    # if request.POST:
    #     username = request.POST.get('username')
    #     password = request.POST.get('password')
    #     state = "deslogueado"
    #     user = authenticate(username=username, password=password)
    #     if user is not None:
    #         if user.is_active:
    #             login(request, user)
    #             state = "You're successfully logged in!"
    #             return HttpResponseRedirect("/administracion/")
         
    #             # else:
    #             # state = "Your account is not active, please contact the site admin."
    #         else:
    #             state = "Your username and/or password were incorrect."
    #     else:
    #         state = 'Incorrect username or password'

    # return render(request, template,{'request': request, 'state': state})

@login_required
@csrf_exempt
def informesFacturacion(request):
    now = datetime.datetime.now()
    mes=now.month
    template = 'discriminacion_iva.html'
    if request.method == "GET":
        if request.GET.get('fecha'):

            mes = request.GET.get('fecha')[-2:]
            # anio = int(request.POST.get('anio'))
            #now = datetime.datetime(anio,mes,1)
            

    if request.method == "POST":
        facturas_recibidas = Factura_recibida.objects.filter(registrado_el__month = mes)
        xlwt.add_palette_colour("color_neto", 0x21)
        xlwt.add_palette_colour("color_iva", 0x22)
        xlwt.add_palette_colour("color_percepciones", 0x23)
        xlwt.add_palette_colour("color_total", 0x24)
        
        estilo_general = xlwt.easyxf('font: name Arial, colour black, bold off; align: wrap on, vert centre, horiz center')
        estilo_empresa = xlwt.easyxf('font: name Arial, colour black, bold off; align: wrap on, horiz left')
        estilo_fecha = xlwt.easyxf('',num_format_str='DD-MMM-YY')
        estilo_moneda = xlwt.easyxf('font: name Arial, colour black, bold off; align: wrap on, vert centre, horiz center',num_format_str='$#,##0.00')
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
        rb = open_workbook("sistema_inges/"+settings.STATIC_URL+'/xls/plantilla/plantilla.xls',formatting_info=True)
        wb = copy(rb)
        wb.set_colour_RGB(0x22, 41, 117, 217)
        wb.set_colour_RGB(0x21, 242, 221, 64)
        wb.set_colour_RGB(0x23, 115, 76, 65)
        wb.set_colour_RGB(0x24, 56, 166, 62)

        estilo_neto = xlwt.easyxf('font: name Arial, bold on; align: wrap on, vert centre, horiz center; pattern: pattern solid, fore_colour color_neto') # 11 * 20, for 11 point
        estilo_iva = xlwt.easyxf('font: name Arial, bold on; align: wrap on, vert centre, horiz center; pattern: pattern solid, fore_colour color_iva')
        estilo_percepciones = xlwt.easyxf('font: name Arial, bold on, height 180; align: wrap on, vert centre, horiz center; pattern: pattern solid, fore_colour color_percepciones')
        estilo_total = xlwt.easyxf('font: name Arial, bold on; align: wrap on, vert centre, horiz center; pattern: pattern solid, fore_colour color_total')
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

        ws.write(0, 3, ARRAY_MESES[now.month - 1]+' '+now.strftime("%Y"), estilo_general)

        i = 3
        for fr in facturas_recibidas:
            ws.write(i, 1, fr.fecha, estilo_fecha)
            ws.write(i, 2, fr.emisor.nombre, estilo_empresa)
            ws.write(i, 3, fr.nro_factura, estilo_general)
            ws.write(i, 4, fr.subtotal, estilo_moneda)
            ws.write(i, 5, fr.impuesto(), estilo_moneda)
            ws.write(i, 6, fr.percepciones_otros, estilo_moneda)
            ws.write(i, 7, fr.total(), estilo_moneda)
            i = i + 1

        estilo_neto = xlwt.easyxf('font: name Arial, bold on; align: wrap on, vert centre, horiz center; pattern: pattern solid, fore_colour color_neto',num_format_str='$#,##0.00') # 11 * 20, for 11 point
        estilo_iva = xlwt.easyxf('font: name Arial, bold on; align: wrap on, vert centre, horiz center; pattern: pattern solid, fore_colour color_iva',num_format_str='$#,##0.00')
        estilo_percepciones = xlwt.easyxf('font: name Arial, bold on; align: wrap on, vert centre, horiz center; pattern: pattern solid, fore_colour color_percepciones',num_format_str='$#,##0.00')
        estilo_total = xlwt.easyxf('font: name Arial, bold on; align: wrap on, vert centre, horiz center; pattern: pattern solid, fore_colour color_total',num_format_str='$#,##0.00')
        ws.write(106, 4, xlwt.Formula("SUM(E4:E105)"), estilo_neto)
        ws.write(106, 5, xlwt.Formula("SUM(F4:F105)"), estilo_iva)
        ws.write(106, 6, xlwt.Formula("SUM(G4:G105)"), estilo_percepciones)
        ws.write(106, 7, xlwt.Formula("SUM(H4:H105)"), estilo_total)
        
        fechaXLS = "InformeSI_"+str(now.day) +"-"+ str(now.month) +"-"+ str(now.year) + ".xls"
        wb.save("sistema_inges/"+settings.STATIC_URL+'/xls/' + fechaXLS)
        return HttpResponseRedirect(settings.STATIC_URL+'/xls/' + fechaXLS)
    
    facturas_emitidas = Factura_emitida.objects.filter(registrado_el__month = mes)
    facturas_recibidas = Factura_recibida.objects.filter(registrado_el__month = mes)
    albaranes_recibidos = Albaran_recibido.objects.filter(registrado_el__month = mes)
    facturacion_iva = 0
    descuento_iva = 0
    total_ingresos = 0
    subtotal_ingresos =0
    f_r_civa = 0
    f_r_siva = 0
    percep_otros = 0
    totalAlb = 0
    for f in facturas_emitidas:
        descuento_iva = descuento_iva + f.impuesto()
        total_ingresos = total_ingresos + f.total
        # subtotal_ingresos = subtotal_ingresos + f.subtotal
        subtotal_ingresos = subtotal_ingresos + 0
    for fr in facturas_recibidas:
        facturacion_iva = facturacion_iva + fr.impuesto()
        f_r_civa = f_r_civa + fr.total()
        f_r_siva = f_r_siva + fr.subtotal
        percep_otros = percep_otros + fr.percepciones_otros
    for ar in albaranes_recibidos:
        totalAlb = totalAlb + ar.total
        
    gasto_c_iva = f_r_civa + totalAlb
    gasto_s_iva = f_r_siva + totalAlb

    return render(request, template,{'request': request, 'fact_iva': facturacion_iva,
        'title': 'Informes', 'desc_iva': descuento_iva, 'gastoCIva': gasto_c_iva,
        'gastoSIva': gasto_s_iva, 'mespy': mes, 'detalleFacturasR': facturas_recibidas,
        'detalleFacturasE': facturas_emitidas, 'detalleAlbaranesR': albaranes_recibidos,
         'percep_otros': percep_otros, 'totalAlb': totalAlb, 'total_ingresos': total_ingresos,
         'subtotal_ingresos': subtotal_ingresos, 'f_r_civa': f_r_civa, 'f_r_siva': f_r_siva}, context_instance=RequestContext(request))

    


@login_required
def facturas_recibidas(request, desde=0, hasta=0):
    template = 'facturas_recibidas.html'
    now = datetime.datetime.now()
    if (desde != 0):
        #cal = calendar.month(now.year, desde)
        #facturas1 = Factura_recibida.objects.all().filter(fecha__month = desde)
        #facturas2 = Factura_recibida.objects.all().filter(fecha__month = hasta)
        #facturas = facturas1 | facturas2
        dsd = datetime.date(now.year, int(desde), 1).strftime("%Y-%m-%d")
        hst = datetime.date(now.year, int(hasta), calendar.monthrange(now.year, int(hasta))[1]).strftime("%Y-%m-%d")
        facturas = Factura_recibida.objects.all().filter(fecha__range = [dsd,hst])
        return render(request, template,{'request': request, 'facturas': facturas})
    else:
        facturas = Factura_recibida.objects.all().filter(fecha__month = now.month)
        return render(request, template,{'request': request, 'facturas': facturas})

@login_required
def addFR(request):
    if request.method == "POST":
        guardar = request.POST.get('save')
        # guardarOtro = request.POST.get('addanother')
        form = Factura_recibidaForm(request.POST)
        if form.is_valid():
            form.save()
            # Commit = False sirvepara guardar los datos del form pero sin guardar
            # en la base de datos.Puede servir para hacer modificaciones antes de guardar.
            # factura = form.save( commit = False )

            # modifico el form y pongo el usuarioactual en el campo usuario
            # factura.usuario = request.user
            # factura.save()
            if guardar is not None:
                return HttpResponseRedirect("/facturas_recibidas/")
            else:
                return HttpResponseRedirect("/facturas_recibidas/add/")
    else:
        #factura = Factura_recibida.objects.all().filter(fecha__month = desde)
        form = Factura_recibidaForm()
    ultimaFactura = Factura_recibida.objects.order_by("-pk").all()[0]
    template = 'cargar_f_r.html'
    # context_instance sirvepara hacer validacion de contexto para evitar
    # ataques en los forms, usar solo para forms.
    return render_to_response(template, context_instance = RequestContext(request,locals()))

@login_required
def xls(request):
    style0 = xlwt.easyxf('font: name Times New Roman, colour red, bold on')
    style1 = xlwt.easyxf('',num_format_str='DD-MMM-YY')
    wb = xlwt.Workbook()
    ws = wb.add_sheet('A Test Sheet',cell_overwrite_ok=True)
    ws.write(0, 0, 'Test', style0)
    ws.write(1, 0, datetime.datetime.now(), style1)
    ws.write(2, 0, 4)
    ws.write(2, 1, 1)
    ws.write(2, 2, xlwt.Formula("A3+B3"))
    wb.save("sistema_inges/"+settings.STATIC_URL+'example.xls')
    return HttpResponseRedirect("/facturas_recibidas/add/")

# Conjunto devistas, el del listado y el del objeto como tal.
from rest_framework import viewsets
from .serializers import FRSerializer

class FRViewSet(viewsets.ModelViewSet):
    queryset = Factura_recibida.objects.all()
    serializer_class = FRSerializer