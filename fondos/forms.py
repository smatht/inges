#encoding:utf-8
from django import forms
from django.forms import SelectMultiple
from django.forms import TextInput
from django.forms import Textarea

from models import OrdenPago


class FondosForm(forms.ModelForm):
    total_valores = forms.CharField(required=False)
    total_a_pagar = forms.CharField(required=False)
    diferencia = forms.CharField(required=False)

    # def save(self, commit=True):
    #     diferencia = self.cleaned_data.get('diferencia', None)
    #     if diferencia != 0:
    #         return super(FondosForm, self).save(commit=False)
    #     else:
    #         return super(FondosForm, self).save(commit=commit)

    class Meta:
        model = OrdenPago
        fields = '__all__'
        widgets = {
            'facturas': SelectMultiple(attrs={'size': '10'})
        }

    class Media:
        js = ('js/filterM2M.js',)
