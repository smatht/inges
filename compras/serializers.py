from .models import Compra
from django.contrib.auth.models import User
from rest_framework import serializers

class CompraSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Compra
    fields = ('id', 'saldo')


