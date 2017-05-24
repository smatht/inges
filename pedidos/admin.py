from django.conf.urls import url
from django.contrib import admin
from django.http import HttpResponseRedirect

from actions import export_OR_as_pdf, save_then_pdf
from pedidos.forms import PedidoForm, PedidoDetalleForm, RemitoForm
from pedidos.models import PedidoDetalle, PedidoCabecera, ExtendUser, RemitoCabecera, RemitoDetalle

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User


class UserInline(admin.StackedInline):
  model = ExtendUser
  can_delete = False
  verbose_name_plural = 'usuarios'


class UserAdmin(BaseUserAdmin):
  inlines = (UserInline,)

class ORDetInline(admin.TabularInline):
  form = PedidoDetalleForm
  model = PedidoDetalle
  extra = 1


class ORCabAdmin(admin.ModelAdmin):
  form = PedidoForm
  list_display = ('id', 'fecha', 'registro', 'proveedor', 'destino', 'remito', 'account_actions')
  list_filter = ('proveedor__nombre_fantasia', 'destino__descripcion_corta')
  search_fields = ('pedidodetalle__descripcion',)
  exclude = ('remitente', )
  inlines = [ORDetInline]
  actions = [export_OR_as_pdf]
  fieldsets = [
    (None, {'fields': ['registro', 'fecha', 'proveedor','destino']}),
    ('Orden de retiro', {
      'description': 'Para extender una orden de retiro complete este campo',
      'fields': ['se_autoriza', 'firmante']}),
    ]

  def detalles(self, obj):
    dets = PedidoDetalle.objects.filter(orden_retiro=obj)
    return dets

  def remito(self, obj):
    rem = RemitoCabecera.objects.filter(pedido=obj)
    if (rem):
      return '<img src="/static/admin/img/icon-yes.gif" alt="True">'
    else:
      return '<img src="/static/admin/img/icon-no.gif" alt="False">'
  remito.allow_tags = True

  def save_model(self, request, obj, form, change):
    if getattr(obj, 'remitente', None) is None:
      obj.remitente = request.user
    if getattr(obj, 'firmante', None) is None:
      obj.firmante = request.user
    obj.save()
    # save_then_pdf(request, obj)

  def render_change_form(self, request, context, *args, **kwargs):
    context['adminform'].form.fields['firmante'].queryset = User.objects.filter(extenduser__habilitarPedido=True)
    context['adminform'].form.fields['firmante'].initial = request.user
    return super(ORCabAdmin, self).render_change_form(request, context, args, kwargs)

  def process_print(self, request, pedido_id, *args, **kwargs):
    qs = PedidoCabecera.objects.get(pk=pedido_id)
    return export_OR_as_pdf(self, request, qs)

  def process_remito(self, request, pedido_id, *args, **kwargs):
    pedido = PedidoCabecera.objects.get(pk=pedido_id)
    rem = RemitoCabecera(pedido=pedido)
    rem.save()
    for qs in PedidoDetalle.objects.filter(orden_retiro=pedido_id).order_by('pk'):
      det = RemitoDetalle(remito=rem, descripcion=qs.descripcion, cantidad=qs.cantidad, medida=qs.medida)
      det.save()
    return HttpResponseRedirect("../../../remitocabecera/%s" % rem.id)

  def get_urls(self):
    urls = super(ORCabAdmin, self).get_urls()
    custom_urls = [
      url(
        r'^(?P<pedido_id>.+)/deposit/$',
        self.admin_site.admin_view(self.process_print),
        name='process-print',
      ),
      url(
        r'^(?P<pedido_id>.+)/remito/$',
        self.admin_site.admin_view(self.process_remito),
        name='process-remito',
      ),
    ]
    return custom_urls + urls


class RemitoDetalleInline(admin.TabularInline):
  form = PedidoDetalleForm
  # template = 'admin/edit_inline/stacked.html'
  model = RemitoDetalle


class RemitoAdmin(admin.ModelAdmin):
  form = RemitoForm
  list_display = ('fecha', 'pedido_ID')
  inlines = [RemitoDetalleInline]
  list_filter = ('fecha',)
  search_fields = ('remitodetalle__descripcion',)
  exclude = ('pedido', 'factura')

  def pedido_ID(self, obj):
    if (obj.pedido):
      return '<a href="../%s/%d">%d</a>' % ('pedidocabecera', obj.pedido.id, obj.pedido.id)
    else:
      return '<img src="/static/admin/img/icon-no.gif" alt="False">'
  pedido_ID.allow_tags = True


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(PedidoCabecera, ORCabAdmin)
admin.site.register(RemitoCabecera, RemitoAdmin)