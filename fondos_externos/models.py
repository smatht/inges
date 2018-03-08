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
    amount = models.FloatField()
    categoryId = models.CharField(max_length=40)
    accountId = models.CharField(max_length=40)
    currencyId = models.CharField(max_length=40)
    paymentType = models.CharField(max_length=30)
    date = models.DateTimeField()
    # cuenta = models.ForeignKey(Cuenta)
    # tipoPago = models.CharField(max_length=50) #type of payment (cash,debit_card,credit_card,transfer,voucher,mobile_payment,web_payment)
    # fecha = models.DateTimeField()
    # notas = models.TextField()
    # estado = models.CharField(max_length=50) #state of record (reconciled, cleared, uncleared, void).
