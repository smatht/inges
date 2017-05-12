'''
  El serializador sirve para dar forma a lo que queremos exponer en nuestra api.
'''
from .models import Registro_factura
from django.contrib.auth.models import User
from rest_framework import serializers

class FRSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Registro_factura
    fields = ('url', 'fecha_factura', 'nro_factura', 'subtotal')


class UserSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = User
    fields = ('url', 'username', 'email')