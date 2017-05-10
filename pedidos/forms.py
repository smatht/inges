#encoding:utf-8
from django.forms import ModelForm
from suit.widgets import SuitDateWidget


class PedidoForm(ModelForm):
  class Meta:
    # model = Registro_factura
    widgets = {
      'fecha': SuitDateWidget,
    }