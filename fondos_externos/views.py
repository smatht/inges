# encoding:utf-8
from django.contrib import messages
from django.shortcuts import redirect
from django.conf import settings
from django.template.context import RequestContext
from django.utils.safestring import mark_safe
from pip._vendor import requests

from fondos.models import Caja, MovCaja, TipoMovCaja
from .models import Cuenta, Registro
from facturacion.models import Registro as Empresa
from .serializers import CuentaSerializer, RegistroSerializer


def save_cuenta(request):
    Cuenta.objects.all().delete()
    # Para saber si esxiste el usuario. Si existe "<Response [200]>"
    # url = 'https://api.budgetbakers.com/api/v1/user/exists/matgs656@gmail.com'
    # headers = {'X-Token': '5a3709ce-acfb-49fb-8b60-b1b9e55ffb51'}
    # r = requests.get(url, headers=headers)
    url = 'https://api.budgetbakers.com/api/v1/accounts'
    headers = {
        'X-Token': '5a3709ce-acfb-49fb-8b60-b1b9e55ffb51',
        'X-User': 'matgs656@gmail.com'
    }
    r = requests.get(url, headers=headers)
    json = r.json()
    serializer = CuentaSerializer(data=json, many=True)
    print(serializer.is_valid())
    serializer.save()
    n = Cuenta.objects.count()
    if n > 0:
        messages.add_message(request, messages.SUCCESS, 'Se han exportado ' + str(n) + ' registros')
    else:
        messages.add_message(request, messages.WARNING,
                             mark_safe("No se ha exportado, por favor <a href='/cuentas-wallet/'>reintente aqui </a> en unos minutos."))
    # if serializer.is_valid():
    #     print('1. Validooo')
    #     serializer.save()
    # else:
    #     Cuenta.objects.all().delete()
    #     serializer.save()
    return redirect('/')


def get_registros(request, idCaja=0):
    cantInsertados = 0
    if (idCaja != 0):
        caja = Caja.objects.get(pk=idCaja)
        yaDescargados = MovCaja.objects.exclude(idWallet=None).values_list('idWallet', flat=True)
        print(yaDescargados)
        # Registro.objects.all().delete()
        url = 'https://api.budgetbakers.com/api/v1/records'
        headers = {
            'X-Token': '5a3709ce-acfb-49fb-8b60-b1b9e55ffb51',
            'X-User': 'matgs656@gmail.com'
        }
        r = requests.get(url, headers=headers)
        json = r.json()
        for j in json:
            if j['accountId'] == caja.idCuentaWallet and j['id'] not in yaDescargados:
                print(j)
                importe = 0
                tipoMovCaja = 0
                if j['amount'] < 0:
                    importe = j['amount'] * (-1)
                    tipoMovCaja = TipoMovCaja.objects.get(pk=10) #HARDCODED
                else:
                    importe = j['amount']
                    tipoMovCaja = TipoMovCaja.objects.get(pk=9)  # HARDCODED
                empresa = Empresa.objects.get(pk=1) #HARDCODED
                fecha = j['date']
                descripcion = 'Wallet: ' + j['note']
                idWallet = j['id']
                mov = MovCaja(caja=caja, empresa=empresa, fecha=fecha, descripcion=descripcion, importe=importe,
                              tipoMovCaja=tipoMovCaja, idWallet=idWallet, operador=request.user)
                mov.save()
                cantInsertados += 1
        # serializer = RegistroSerializer(data=json, many=True)
        # serializer.save()
        # if serializer.is_valid():
        #     print('1. Validooo')
        #     serializer.save()
        # else:
        #     Cuenta.objects.all().delete()
        #     serializer.save()
    # messages.add_message(request, messages.SUCCESS, 'Se han exportado 5 registros')
    # messages.add_message(request, messages.WARNING,
    #                      mark_safe("Sin respuesta del servicio externo, por favor <a href='/administracion/fondos/movcaja/'>reintente aqui </a> en unos minutos."))
    # messages.add_message(request, messages.ERROR, 'Error grave. No se ha realizado la exportación')
    if cantInsertados > 0:
        messages.add_message(request, messages.INFO, 'Se han exportado ' + str(cantInsertados) + ' registros')
    if cantInsertados == 0:
        messages.add_message(request, messages.WARNING, mark_safe("No se encontraron registros. <a href='/registros-wallet/"+ str(idCaja) +"'>Reintente aqui.</a>"))
    return redirect('/administracion/fondos/movcaja/')
