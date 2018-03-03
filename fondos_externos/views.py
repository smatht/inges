from django.shortcuts import redirect
from django.conf import settings
from django.template.context import RequestContext
from pip._vendor import requests

from .models import Cuenta
from .serializers import CuentaSerializer


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
    serializer.save()
    # if serializer.is_valid():
    #     print('1. Validooo')
    #     serializer.save()
    # else:
    #     Cuenta.objects.all().delete()
    #     serializer.save()
    return redirect('/')

