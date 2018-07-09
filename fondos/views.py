import calendar
import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from fondos.forms import ConfiguracionReporteCaja


@login_required
@csrf_exempt
def ReporteCajaView(request):
    form = ConfiguracionReporteCaja
    template = 'reporte_caja.html'
    now = datetime.date.today()

    if request.method == "GET":
        if request.GET.get('desde') and request.GET.get('hasta'):
            desde = datetime.date(request.GET.get('desde'))
            hasta = datetime.date(request.GET.get('hasta'))
        else:
            desde = datetime.date(now.year, now.month, 1)
            hasta = datetime.date(now.year, now.month, calendar.monthrange(now.year, now.month)[1])



    return render(request, template, {'title': 'Reporte de caja', 'form': form})
