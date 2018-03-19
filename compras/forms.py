#encoding:utf-8
from django import forms
from django.forms import ModelForm
from django.forms import Select
from django.forms import Textarea
from django.forms.widgets import TextInput
from suit.widgets import SuitDateWidget, NumberInput, SuitSplitDateTimeWidget, EnclosedInput

from fondos.models import TipoCaja
from models import Compra


class PedidoForm(ModelForm):
  class Meta:
    # model = Registro_factura
    widgets = {
      'fechaPedido': SuitDateWidget,
    }

class PedidoItemForm(ModelForm):
  class Meta:
    # model = Registro_factura
    widgets = {
      'sDescripcion': Textarea(attrs={'style': 'width: 370px', 'rows':2}),
      'producto': Select(attrs={'style': 'width: 400px'}),
      'sCantidad': NumberInput(attrs={'step': 0.1, 'style': 'width: 50px', 'min':'0'}),
      # 'precioUnitario': NumberInput(attrs={'step': 0.1, 'style': 'width: 75px', 'min':'0'}),
      # 'importe': NumberInput(attrs={'step': 0.1, 'style': 'width: 75px', 'min':'0'}),
      'medida': Select(attrs={'style': 'width: 150px'}),
    }

class RemitoForm(ModelForm):
  class Meta:
    # model = Registro_factura
    widgets = {
      'fechaRemito': SuitDateWidget,
    }


class CompraForm(forms.ModelForm):
    qTCaja = TipoCaja.objects.all()
    generarMov = forms.BooleanField(label='Generar movimiento caja', initial=True, required=False)
    tipoCaja = forms.ModelChoiceField(queryset=qTCaja, required=False, label='Caja')

    class Meta:
        model = Compra
        fields = '__all__'
        widgets = {
            'sucursal': TextInput(attrs={'style': 'width: 50px', 'maxlength':'4'}),
            'numDoc': TextInput(attrs={'style': 'width: 150px', 'maxlength':'8'}),
            'cantidad': TextInput(attrs={'style': 'width: 40px'}),
            'alicuota': Select(attrs={'style': 'width: 100px'}),
            'precio_unitario': EnclosedInput(prepend='$', attrs={'style': 'width: 60px'}),
            'descripcion': Textarea(attrs={'style': 'width: 370px', 'rows': 1}),
        }


class CompraItemForm(ModelForm):
  class Meta:
    # model = Registro_factura
    widgets = {
      'cantidad': TextInput(attrs={'style': 'width: 40px'}),
      'alicuota': Select(attrs={'style': 'width: 100px'}),
    }