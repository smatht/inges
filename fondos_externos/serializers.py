from rest_framework import serializers
from .models import Cuenta, Registro


# class CuentaListSerializer(serializers.ListSerializer):
#     def update(self, instance, validated_data):
#         pass
    #     instance.id = validated_data.get('id', instance.id)
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.color = validated_data.get('color', instance.color)
    #     instance.excludeFromStats = validated_data.get('excludeFromStats', instance.excludeFromStats)
    #     instance.gps = validated_data.get('gps', instance.gps)
    #     instance.initAmount = validated_data.get('initAmount', instance.initAmount)
    #     instance.position = validated_data.get('position', instance.position)
    #     instance.save()
    #     return instance


class CuentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuenta
        # list_serializer_class = CuentaListSerializer
        fields = ('id', 'name', 'color', 'excludeFromStats', 'gps', 'initAmount', 'position')

    def create(self, validated_data):
        # cuenta = Cuenta(idWallet=self.validated_data['id'],
        #                 name=self.validated_data['name'],
        #                 color=self.validated_data['color'],
        #                 excludeFromStats= self.validated_data['excludeFromStats'],
        #                 gps=self.validated_data['gps'],
        #                 initAmount=self.validated_data['initAmount'],
        #                 position=self.validated_data['position'])
        cuenta = Cuenta(**validated_data)
        cuenta.save()
        return cuenta

    def update(self, instance, validated_data):
        pass
    #     instance.id = validated_data.get('id', instance.id)
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.color = validated_data.get('color', instance.color)
    #     instance.excludeFromStats = validated_data.get('excludeFromStats', instance.excludeFromStats)
    #     instance.gps = validated_data.get('gps', instance.gps)
    #     instance.initAmount = validated_data.get('initAmount', instance.initAmount)
    #     instance.position = validated_data.get('position', instance.position)
    #     instance.save()
    #     return instance



class RegistroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registro
        # list_serializer_class = CuentaListSerializer
        fields = ('id', 'amount', 'categoryId', 'accountId', 'currencyId', 'paymentType', 'date', 'note', 'recordState')

    def create(self, validated_data):
        # cuenta = Cuenta(idWallet=self.validated_data['id'],
        #                 name=self.validated_data['name'],
        #                 color=self.validated_data['color'],
        #                 excludeFromStats= self.validated_data['excludeFromStats'],
        #                 gps=self.validated_data['gps'],
        #                 initAmount=self.validated_data['initAmount'],
        #                 position=self.validated_data['position'])
        registro = Registro(**validated_data)
        registro.save()
        return registro