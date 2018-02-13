from rest_framework import serializers

from models import Producto


class PROSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Producto
    fields = ('url', 'id', 'descripcion', 'precio')