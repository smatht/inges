from facturacion.models import Factura_recibida, Iva, Empresa
from django.shortcuts import render_to_response, get_object_or_404, HttpResponse, render, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from models import *
import datetime
import calendar
from facturacion.forms import *
from django.template.context import RequestContext

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
def informesFacturacion(request):
    now = datetime.datetime.now()
    mes=now.month
    if request.method == "GET":
        if request.GET.get('fecha'):

            mes = request.GET.get('fecha')[-2:]
            # anio = int(request.POST.get('anio'))
            #now = datetime.datetime(anio,mes,1)
        
    facturas_emitidas = Factura_emitida.objects.filter(registrado_el__month = mes)
    facturas_recibidas = Factura_recibida.objects.filter(registrado_el__month = mes)
    facturacion_iva = 0;
    descuento_iva = 0;
    gasto_c_iva = 0
    gasto_s_iva = 0
    percep_otros = 0
    for f in facturas_emitidas:
        descuento_iva = descuento_iva + f.iva()
    for fr in facturas_recibidas:
        facturacion_iva = facturacion_iva + fr.impuesto()
        gasto_c_iva = gasto_c_iva + fr.total()
        gasto_s_iva = gasto_s_iva + fr.neto
        percep_otros = percep_otros + fr.percepciones_otros
    template = 'discriminacion_iva.html'
    
    return render(request, template,{'request': request, 'fact_iva': facturacion_iva,
        'title': 'Informes', 'desc_iva': descuento_iva, 'gastoCIva': gasto_c_iva,
        'gastoSIva': gasto_s_iva, 'mespy': mes, 'detalleFacturasR': facturas_recibidas,
        'detalleFacturasE': facturas_emitidas, 'percep_otros': percep_otros})



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

