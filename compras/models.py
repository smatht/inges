from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.datetime_safe import datetime
from django.utils.html import format_html

from inges.facturacion.models import Registro

from inges.facturacion.models import Proveedor

from inges.proyectos.models import Obra


class Pedido(models.Model):
    # cuit = lambda: Registro.objects.get(cuit='23144591119')
    registro = models.ForeignKey(Registro, default=1, verbose_name='Empresa')
    fecha = models.DateField(default=datetime.datetime.now)
    proveedor = models.ForeignKey(Proveedor)
    se_autoriza = models.ForeignKey(User, related_name='toUser', verbose_name='Se autoriza a', blank=True, null=True)
    destino = models.ForeignKey(Obra, verbose_name='Obra')
    firmante = models.ForeignKey(User, related_name='fromUser', help_text='Persona que autoriza', blank=True, null=True)
    remitente = models.ForeignKey(User, related_name='registerUser', help_text='Persona que registra')

    class Meta:
        ordering = ['-fecha']
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

    def __unicode__(self):
        return unicode('[' + str(self.pk) + '] ' + self.fecha.strftime('%d/%m/%Y') + ' - ' + str(self.proveedor) +
                       ' (' + str(self.destino) + ')')
        # return unicode(self.fecha.strftime('%d/%m/%Y'))


    # Botones de acciones para pedidos
    def account_actions(self):
        return format_html(
            '<a class="btn" href="{}" target="_blank" title="Mostrar pdf"><i class="icon-print"></i></a>'
            '<a class="btn" id="add_id_remito" href="{}" title="Agregar remito" onclick="return showRelatedObjectPopup(this, 1100, 500);"><i class="icon-check"></i></a>',
            reverse('admin:process-print', args=[self.pk]),
            reverse('admin:process-remito', args=[self.pk]),
        )

    account_actions.short_description = 'Acciones'
    account_actions.allow_tags = True


class PedidoItem(models.Model):
    orden_retiro = models.ForeignKey(Pedido)
    descripcion = models.CharField(max_length=300)
    cantidad = models.CharField(max_length=10)
    UNIDAD_MEDIDA = (
        ('un', 'unidades'),
        ('mt', 'metros'),
        ('m2', 'metros cuadrados'),
        ('m3', 'metros cubicos'),
        ('gr', 'gramos'),
        ('kg', 'kilogramos'),
        ('lt', 'litros'),
        ('ml', 'milimetros'),
        ('km', 'kilómetros'),
        ('tn', 'toneladas'),
        ('om', 'otras medidas'),
    )
    medida = models.CharField(
        max_length=2,
        choices=UNIDAD_MEDIDA,
        default='un',
    )

    class Meta:
        verbose_name = 'Detalle de pedido'
        verbose_name_plural = 'Detalle de pedido'

    def __unicode__(self):
        return unicode(self.descripcion + ' [' + str(self.cantidad) + ']')

# Create your models here.
