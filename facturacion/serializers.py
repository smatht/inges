'''
	El serializador sirve para dar forma a lo que queremos exponer en nuestra api.
'''
from .models import Factura_recibida
from django.contrib.auth.models import User
from rest_framework import serializers

class FRSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Factura_recibida
		fields = ('url', 'fecha', 'nro_factura', 'subtotal', 'percepciones_otros')


class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('url', 'username', 'email')