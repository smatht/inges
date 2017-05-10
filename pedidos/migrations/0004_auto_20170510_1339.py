# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0003_auto_20170509_1843'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedidodetalle',
            name='medida',
            field=models.CharField(default=b'un', max_length=2, choices=[(b'un', b'unidades'), (b'mt', b'metros'), (b'm2', b'metros cuadrados'), (b'm3', b'metros cubicos'), (b'gr', b'gramos'), (b'kg', b'kilogramos'), (b'lt', b'litros'), (b'ml', b'milimetros'), (b'km', b'kil\xc3\xb3metros'), (b'tn', b'toneladas'), (b'om', b'otras medidas')]),
        ),
        migrations.AlterField(
            model_name='pedidocabecera',
            name='destino',
            field=models.ForeignKey(verbose_name=b'Obra / Destino', to='proyectos.Obra'),
        ),
        migrations.AlterField(
            model_name='pedidocabecera',
            name='se_autoriza',
            field=models.ForeignKey(related_name='toUser', verbose_name=b'Se autoriza a', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
