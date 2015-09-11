#encoding:utf-8
from django.forms import ModelForm
from django import forms
from facturacion.models import Registro_factura
from suit.widgets import SuitDateWidget
from suit.widgets import AutosizedTextarea


class FacturaForm(ModelForm):
    class Meta:
    	# model = Registro_factura
        widgets = {

            # You can also specify html attributes
            'detalle': AutosizedTextarea(attrs={'rows': 3, 'class': 'input-xlarge'}),
        }

