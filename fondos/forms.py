#encoding:utf-8
import calendar
import datetime

from django import forms
from django.forms import SelectMultiple
from django.forms import TextInput
from django.forms import Textarea
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.forms.extras import SelectDateWidget
from django.utils.safestring import mark_safe
from suit.widgets import AutosizedTextarea, SuitDateWidget

from fondos_externos.models import Cuenta
from mantenimiento.models import Configuracion
from models import OrdenPago, Caja, TipoCaja
from proyectos.models import Obra

# Pone radio select en horizontal
class HorizontalRadioRenderer(forms.RadioSelect.renderer):
  def render(self):
    return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))

class OPForm(forms.ModelForm):
    total_valores = forms.CharField(required=False, initial=0)
    total_a_pagar = forms.CharField(required=False, initial=0)
    diferencia = forms.CharField(required=False, initial=0)
    imprimir_recibo = forms.BooleanField(initial=False, required=False)
    tipoCaja = forms.ModelChoiceField(queryset=TipoCaja.objects.all(), required=False, label="Tipo caja")
    obra = forms.ModelChoiceField(queryset=Obra.objects.all(), required=False)
    comentario = forms.CharField(widget=forms.Textarea(attrs={'rows':4, 'class': 'input-xxlarge'}), required=False)
    TIPO = (
        (0, 'Pago facturas'),
        (1, 'Pago a cuenta'),
    )
    tipoPago = forms.ChoiceField(
        choices=TIPO,
        widget=forms.RadioSelect(renderer=HorizontalRadioRenderer),
        initial=0,
        label='',
        required=False,

    )
    # pagoACuenta = forms.BooleanField(label='Pago a cuenta', required=False)

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
        ch = super(CajaForm, self).changed_data
        if 'tipoCaja' in ch:
            try:
                cja = Caja.objects.get(tipoCaja=cleaned_data.get('tipoCaja'), destino=cleaned_data.get('destino'), fCierre=None)
                raise forms.ValidationError('La caja: "' + cleaned_data.get('tipoCaja').descripcion + '" Obra: "' +
                                            cleaned_data.get('destino').descripcion_corta + '" ya existe. Cierrela antes de abrir una nueva.')
            except ObjectDoesNotExist:
                return
        if 'destino' in ch:
            try:
                cja = Caja.objects.get(tipoCaja=cleaned_data.get('tipoCaja'), destino=cleaned_data.get('destino'), fCierre=None)
                raise forms.ValidationError('La caja: "' + cleaned_data.get('tipoCaja').descripcion + '" Obra: "' +
                                            cleaned_data.get('destino').descripcion_corta + '" ya existe. Cierrela antes de abrir una nueva.')
            except ObjectDoesNotExist:
                return

    class Meta:
        model = Caja
        fields = '__all__'


class ConfiguracionReporteCaja(forms.Form):
    # VARS
    now = datetime.date.today()
    first = datetime.date(now.year, now.month, 1)
    last = datetime.date(now.year, now.month, calendar.monthrange(now.year, now.month)[1])
    tipoCajaDefecto = Configuracion.objects.get(pk=1).general_tipoCaja
    obraCajaDefecto = Configuracion.objects.get(pk=1).general_obraDefault
    # FIELDS
    desde = forms.DateField(label='Desde: ', initial=first, widget=forms.TextInput(attrs={"type": "date"}))
    hasta = forms.DateField(label='Hasta: ', initial=last, widget=forms.TextInput(attrs={"type": "date"}))
    tipoCaja = forms.ModelChoiceField(queryset=TipoCaja.objects.all(), label="Tipo caja: ", initial=tipoCajaDefecto.pk)
    obraCaja = forms.ModelChoiceField(queryset=Obra.objects.all(), label="Obra: ", initial=obraCajaDefecto)
    ver_todo = forms.BooleanField(initial=False, label='Ver todo: ', required=False)

    # class Meta:
    #     widgets = {
    #         'desde': TextInput(attrs={'type': 'date', })
    #     }
