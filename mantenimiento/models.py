from django.contrib.auth.models import User
from django.db import models


# Claser que extiende al modelo de usuario de Django
class ExtendUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dni = models.IntegerField(blank=True, null=True)
    habilitarPedido = models.BooleanField(default=False, verbose_name='Habilitar orden de retiro',
                                          help_text='(Marque este campo en caso de que el usuario pueda generar '
                                                    'una orden de retiro con su firma)')

# Create your models here.
