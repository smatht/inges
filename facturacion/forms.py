#encoding:utf-8
from django.forms import ModelForm
from django import forms
from facturacion.models import Factura_recibida

class Factura_recibidaForm(ModelForm):
	class Meta:
		model = Factura_recibida
		# excluir un campo del form
		# exclude = ("iva","usuario",)
