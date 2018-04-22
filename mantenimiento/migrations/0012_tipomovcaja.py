# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def update_contentypes(apps, schema_editor):
    """
    Updates content types.
    We want to have the same content type id, when the model is moved and renamed.
    """
    ContentType = apps.get_model('contenttypes', 'ContentType')
    db_alias = schema_editor.connection.alias

    # Move the ModelThatShouldBeMoved model to app2 and rename to ModelThatWasMoved
    qs = ContentType.objects.using(db_alias).filter(app_label='fondos', model='tipomovcaja')
    qs.update(app_label='mantenimiento', model='tipomovcaja')


def update_contentypes_reverse(apps, schema_editor):
    """
    Reverts changes in content types.
    """
    ContentType = apps.get_model('contenttypes', 'ContentType')
    db_alias = schema_editor.connection.alias

    # Move the ModelThatWasMoved model to app1 and rename to ModelThatShouldBeMoved
    qs = ContentType.objects.using(db_alias).filter(app_label='mantenimiento')
    qs.update(app_label='fondos')


class Migration(migrations.Migration):

    dependencies = [
        ('mantenimiento', '0011_auto_20180203_1427'),
        ('fondos', '0022_auto_20180421_1759'),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    state_operations = [
        migrations.CreateModel(
            name='TipoMovCaja',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=75)),
                ('suma', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['pk'],
                'verbose_name': 'Tipo movimiento',
                'verbose_name_plural': 'Tipo movimiento',
            },
        ),
    ]

    database_operations = [
        migrations.RunPython(update_contentypes, update_contentypes_reverse),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            state_operations=state_operations,
            database_operations=database_operations
        ),
    ]
