import calendar
import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from fondos.forms import ConfiguracionReporteCaja
from fondos.models import MovCaja, TipoCaja, Caja
from mantenimiento.models import Configuracion
from proyectos.models import Obra


@login_required
@csrf_exempt
def ReporteCajaView(request):
    form = ConfiguracionReporteCaja(request.GET or None)
    template = 'reporte_caja.html'
    now = datetime.date.today()
    config = Configuracion.objects.get(pk=1)
    caja = Caja.objects.all()
    queryset = MovCaja.objects.all()

    if form.is_valid():
        data = form.cleaned_data
        d = data['desde']
        h = data['hasta']
        tc = data['tipoCaja']
        oc = data['obraCaja']
        # desde = datetime.date(int(d[:4]), int(d[5:7]), int(d[8:10]))
        # hasta = datetime.date(int(h[:4]), int(h[5:7]), int(h[8:10]))
        caja = caja.get(tipoCaja=tc, destino=oc, fCierre=None)
        caja.saldo = caja.saldo()
        if data['ver_todo']:
            queryset = queryset.filter(caja__destino=caja.destino, caja__tipoCaja=caja.tipoCaja)
        else:
            queryset = queryset.filter(fecha__range=(d, h), caja__destino=caja.destino, caja__tipoCaja=caja.tipoCaja)

    else:
        desde = datetime.date(now.year, now.month, 1)
        hasta = datetime.date(now.year, now.month, calendar.monthrange(now.year, now.month)[1])
        tc = config.general_tipoCaja
        oc = config.general_obraDefault
        caja = caja.get(tipoCaja=tc, destino=oc, fCierre=None)
        caja. saldo = caja.saldo()
        queryset = queryset.filter(fecha__range=(desde, hasta), caja__destino=caja.destino, caja__tipoCaja=caja.tipoCaja)

    # if request.method == "GET":
    #     if request.GET.get('desde') and request.GET.get('hasta'):
    #         desde = datetime.date(request.GET.get('desde'))
    #         hasta = datetime.date(request.GET.get('hasta'))
    #     else:
    #         desde = datetime.date(now.year, now.month, 1)
    #         hasta = datetime.date(now.year, now.month, calendar.monthrange(now.year, now.month)[1])



    return render(request, template, {'title': 'Reporte de caja', 'form': form, 'caja': caja, 'movimientos': queryset})
