from django.db import models

class UnidadesMedida(models.Model):
    descripcion = models.CharField(max_length=20)
    descripcionCorta = models.CharField(max_length=5)
    # UNIDAD_MEDIDA = (
    #     ('un', 'unidades'),
    #     ('mt', 'metros'),
    #     ('m2', 'metros cuadrados'),
    #     ('m3', 'metros cubicos'),
    #     ('gr', 'gramos'),
    #     ('kg', 'kilogramos'),
    #     ('lt', 'litros'),
    #     ('ml', 'milimetros'),
    #     ('km', 'kilómetros'),
    #     ('tn', 'toneladas'),
    #     ('om', 'otras medidas'),
    # )
    # medida = models.CharField(
    #     max_length=2,
    #     choices=UNIDAD_MEDIDA,
    #     default='un',
    # )

# Create your models here.
