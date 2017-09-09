#encoding:utf-8
from django.forms import ModelForm
from django.forms import SelectMultiple
from django.forms import TextInput
from django.forms import Textarea


class ProductoForm(ModelForm):
    class Meta:
        # model = Registro_factura
        widgets = {
            'descripcion': TextInput(attrs={'style': 'width: 500px'}),
            # 'descripcionCorta': TextInput(attrs={'style': 'width: 200px'}),
            'proveedor': SelectMultiple(attrs={'style': 'overflow:hidden'})
    }

    class Media:
        js = ('js/selectMultipleProved.js',)
