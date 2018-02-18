#encoding:utf-8
from django.forms import ModelForm
from django.forms import SelectMultiple
from django.forms import TextInput
from django.forms import Textarea


class FondosForm(ModelForm):
    class Meta:
        # model = Registro_factura
        widgets = {
            'facturas': SelectMultiple(attrs={'size': '10'})
    }
