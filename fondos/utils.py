from django.core.exceptions import ObjectDoesNotExist

from fondos.models import Caja, TipoCaja


def getOrOpenCaja(tipoCaja, obra):
    try:
        cja = Caja.objects.get(tipoCaja=tipoCaja, destino=obra, fCierre=None)
    except ObjectDoesNotExist:
        cja = abrirCaja(obra, tipoCaja)
    return cja


def abrirCaja(obra, tipoCaja = None):
    if tipoCaja is None:
        tipoCaja = TipoCaja.objects.get(pk=1)
    cja = Caja(tipoCaja=tipoCaja, destino=obra)
    cja.save()
    return cja


