from rest_framework import serializers
from .models import Cuenta

class CuentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuenta
        fields = ('id', 'name', 'color', 'excludeFromStats', 'gps', 'initAmount', 'position')


class CuentaSerializer2(serializers.Serializer):
    id = serializers.CharField()
    name = serializers.CharField()
    color = serializers.CharField()
    excludeFromStats = serializers.BooleanField()
    gps = serializers.BooleanField()
    initAmount = serializers.FloatField()
    position = serializers.IntegerField()

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Cuenta.objects.create(**validated_data)