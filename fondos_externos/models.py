import datetime
from django.db import models

class Cuenta(models.Model):
    id = models.CharField(primary_key=True, max_length=40)
    name = models.CharField(max_length=50)
    color = models.CharField(null=True, blank=True, max_length=10)
    excludeFromStats = models.BooleanField()
    gps = models.BooleanField()
    initAmount = models.FloatField(default=0)
    position = models.IntegerField()

    def __unicode__(self):
        return format(self.name)


class Categoria(models.Model):
    id = models.CharField(primary_key=True, max_length=40)
    nombre = models.CharField(max_length=75)


class Registro(models.Model):
    id = models.CharField(primary_key=True, max_length=40)
    amount = models.FloatField(null=True)
    categoryId = models.CharField(max_length=40, null=True)
    accountId = models.CharField(max_length=40, null=True)
    currencyId = models.CharField(max_length=40, null=True)
    paymentType = models.CharField(max_length=30, null=True)
    date = models.DateTimeField(default=datetime.datetime.now)
    note = models.CharField(max_length=150, null=True, blank=True)
    recordState = models.CharField(max_length=30, null=True, blank=True)
