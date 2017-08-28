#encoding:utf-8
from django.forms import ModelForm
from django.forms import Select
from django.forms import Textarea
from suit.widgets import SuitDateWidget, NumberInput, SuitSplitDateTimeWidget


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
      # 'descripcion': Textarea(attrs={'style': 'width: 370px', 'rows':2}),
      'producto': Select(attrs={'style': 'width: 400px'}),
      'cantidad': NumberInput(attrs={'step': 0.1, 'style': 'width: 50px', 'min':'0'}),
      'precioUnitario': NumberInput(attrs={'step': 0.1, 'style': 'width: 75px', 'min':'0'}),
      'importe': NumberInput(attrs={'step': 0.1, 'style': 'width: 75px', 'min':'0'}),
      'medida': Select(attrs={'style': 'width: 150px'}),
    }

class RemitoForm(ModelForm):
  class Meta:
    # model = Registro_factura
    widgets = {
      'fechaRemito': SuitDateWidget,
    }