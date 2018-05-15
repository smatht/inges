#encoding:utf-8
from django import forms
from django.forms import SelectMultiple
from django.forms import TextInput
from django.forms import Textarea
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from suit.widgets import AutosizedTextarea

from fondos_externos.models import Cuenta
from models import OrdenPago, Caja, TipoCaja
from proyectos.models import Obra


class OPForm(forms.ModelForm):
    total_valores = forms.CharField(required=False, initial=0)
    total_a_pagar = forms.CharField(required=False, initial=0)
    diferencia = forms.CharField(required=False, initial=0)
    imprimir_recibo = forms.BooleanField(initial=False, required=False)
    tipoCaja = forms.ModelChoiceField(queryset=TipoCaja.objects.all(), required=False, label="Tipo caja")
    obra = forms.ModelChoiceField(queryset=Obra.objects.all(), required=False)
    comentario = forms.CharField(widget=forms.Textarea(attrs={'rows':4, 'class': 'input-xxlarge'}), required=False)

    # widgets = {
    #     # You can also specify html attributes
    #     'comentario': Textarea(attrs={'class': 'input-xlarge'}),
    # }

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
        js = ('js/jquery.textcomplete.min.js', 'js/filterM2M.js', 'js/algoliasearch.jquery.min.js', 'js/template_autocomplete.js')


class CajaForm(forms.ModelForm):
    cuentaWallet = forms.ModelChoiceField(queryset=Cuenta.objects.all(), required=False)

    def clean(self):
        cleaned_data = super(CajaForm, self).clean()
        try:
            cja = Caja.objects.get(tipoCaja=cleaned_data.get('tipoCaja'), destino=cleaned_data.get('destino'), fCierre=None)
            raise forms.ValidationError('La caja: "' + cleaned_data.get('tipoCaja').descripcion + '" Obra: "' +
                                        cleaned_data.get('destino').descripcion_corta + '" ya existe. Cierrela antes de abrir una nueva.')
        except ObjectDoesNotExist:
            return


    class Meta:
        model = Caja
        fields = '__all__'
