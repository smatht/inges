#encoding:utf-8
from django.forms import ModelForm
from django.forms import Textarea


class ObrasForm(ModelForm):
    class Meta:
        # model = Registro_factura
        widgets = {
            'descripcion': Textarea(attrs={'cols' :40, 'rows' :3}),
        }