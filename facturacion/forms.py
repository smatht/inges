#encoding:utf-8

from django.forms import ModelForm
# from django import forms
# from facturacion.models import Registro_factura
# from suit.widgets import SuitDateWidget
from django.forms import Select
from django.forms import TextInput
from django.forms import Textarea
from suit.widgets import AutosizedTextarea, NumberInput


class FacturaForm(ModelForm):
  class Meta:
    # model = Registro_factura
    widgets = {
      # You can also specify html attributes
      'observaciones': AutosizedTextarea(attrs={'rows': 3, 'class': 'input-xlarge'}),
    }

class FacturaDetalleForm(ModelForm):
  class Meta:
    # model = Registro_factura
    widgets = {
      'descripcion': Textarea(attrs={'rows': 1, 'style': 'width: 370px'}),
      'cantidad': NumberInput(attrs={'style': 'width: 50px'}),
      'alicuota': Select(attrs={'style': 'width: 70px'}),
      'precio_unitario': NumberInput(attrs={'step': 0.10, 'style': 'width: 60px'}),
      'total': NumberInput(attrs={'step': 0.10, 'style': 'width: 60px'})
    }