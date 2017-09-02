from django.conf.urls import url
from django.contrib import admin
from compras.models import PedidoItem, Pedido, Remito, RemitoItem
from functools32 import update_wrapper
from pedidos.models import ExtendUser
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from actions import export_OR_as_pdf, save_then_pdf
from compras.forms import PedidoItemForm, PedidoForm, RemitoForm
from stock.models import Producto
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django_extensions.admin import ForeignKeyAutocompleteAdmin, ForeignKeyAutocompleteTabularInline




class UserInline(admin.StackedInline):
  model = ExtendUser
  can_delete = False
  verbose_name_plural = 'usuarios'

# @admin.register(User)
class UserAdmin(BaseUserAdmin):
  inlines = (UserInline,)

class PedidoItemInline(ForeignKeyAutocompleteTabularInline):
  form = PedidoItemForm
  model = PedidoItem
  related_search_fields = {
    'producto': ('descripcion',),
  }
  # # fields = ('producto',)
  extra = 10


@admin.register(Pedido)
class PedidoAdmin(ForeignKeyAutocompleteAdmin):
  form = PedidoForm
  list_display = ('id', 'fechaPedido', 'registro', 'proveedor', 'destino', 'recepcion', 'account_actions')
  list_filter = ('proveedor__nombre_fantasia', 'destino__descripcion_corta', 'fechaPedido')
  search_fields = ('pedido__producto__descripcion',)
  exclude = ('remitente', 'usuario', 'anulado', 'fechaCarga')
  inlines = [PedidoItemInline]
  actions = [export_OR_as_pdf]
  fieldsets = [
    (None, {'fields': ['registro', 'fechaPedido', 'proveedor','destino', 'generaRemito']}),
    ('Orden de retiro', {
      'description': 'Para extender una orden de retiro complete este campo',
      'fields': ['se_autoriza', 'firmante']}),
    ]

  def wrap(self, view):
    def wrapper(*args, **kwargs):
      return self.admin_site.admin_view(view)(*args, **kwargs)
    wrapper.model_admin = self
    return update_wrapper(wrapper, view)

  def detalles(self, obj):
    dets = PedidoItem.objects.filter(pedido=obj)
    return dets

  def recepcion(self, obj):
    rem = Remito.objects.filter(pedido=obj)
    ped_det = PedidoItem.objects.filter(pedido=obj)
    cant_ped_det = 0
    cant_rem_det = 0

    rem_det_is_false = RemitoItem.objects.filter(remito=rem, confirmacion=False)
    for d in ped_det:
      cant_ped_det += float(d.cantidad)
    for r in rem:
      for d in RemitoItem.objects.filter(remito=r):
        cant_rem_det += float(d.cantidad)

    if (rem):
      if ((cant_ped_det != cant_rem_det) | (len(rem_det_is_false) >= 1)):
        return '<img src="/static/admin/img/icon-casi-yes.gif" alt="True">'
      else:
        return '<img src="/static/admin/img/icon-yes.gif" alt="True">'
    else:
      return '<img src="/static/admin/img/icon-casi-no.gif" alt="False">'
  recepcion.allow_tags = True

  def save_model(self, request, obj, form, change):
    if getattr(obj, 'remitente', None) is None:
      obj.remitente = request.user
    if getattr(obj, 'firmante', None) is None:
      obj.firmante = request.user
    if getattr(obj, 'usuario', None) is None:
      obj.usuario = request.user
    obj.save()
    # save_then_pdf(request, obj)

  def render_change_form(self, request, context, *args, **kwargs):
    context['adminform'].form.fields['firmante'].queryset = User.objects.filter(extenduser__habilitarPedido=True)
    context['adminform'].form.fields['firmante'].initial = request.user
    return super(PedidoAdmin, self).render_change_form(request, context, args, kwargs)

  def process_print(self, request, pedido_id, *args, **kwargs):
    qs = Pedido.objects.get(pk=pedido_id)
    return export_OR_as_pdf(self, request, qs)

  def process_remito(self, request, pedido_id, *args, **kwargs):
    pedido = Pedido.objects.get(pk=pedido_id)
    rem = Remito(pedido=pedido, registro=pedido.registro, proveedor=pedido.proveedor, destino=pedido.destino)
    rem.save()
    for qs in PedidoItem.objects.filter(pedido=pedido_id).order_by('pk'):
      det = RemitoItem(remito=rem, producto=qs.producto, cantidad=qs.cantidad, unidades=qs.unidades)
      det.save()
    return HttpResponseRedirect("../../../remito/%s?_popup=1" % rem.id)

  def get_urls(self):
    urls = super(PedidoAdmin, self).get_urls()
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


class RemitoItemInline(ForeignKeyAutocompleteTabularInline):
  form = PedidoItemForm
  # template = 'admin/edit_inline/stacked.html'
  model = RemitoItem
  extra = 10
  related_search_fields = {
    'producto': ('descripcion',),
  }
  # fields = ('producto',)

@admin.register(Remito)
class RemitoAdmin(ForeignKeyAutocompleteAdmin):
  ForeignKeyAutocompleteAdmin.model = Producto
  form = RemitoForm
  list_display = ('fechaRemito', 'proveedor', 'pedido_ID')
  inlines = [RemitoItemInline]
  list_filter = ('fechaRemito', 'proveedor__nombre_fantasia', 'pedido__id')
  search_fields = ('remitoitem__producto__descripcion',)
  exclude = ('factura', 'usuario', 'origen', 'afectaStock', 'fechaCarga')

  def save_model(self, request, obj, form, change):
    if getattr(obj, 'usuario', None) is None:
      obj.usuario = request.user
    obj.save()

  def pedido_ID(self, obj):
    if (obj.pedido):
      return '<a href="../%s/%d">%d</a>' % ('pedido', obj.pedido.id, obj.pedido.id)
    else:
      return '<img src="/static/admin/img/icon-casi-no.gif" alt="False">'
  pedido_ID.allow_tags = True


  def wrap(self, view):
    def wrapper(*args, **kwargs):
      return self.admin_site.admin_view(view)(*args, **kwargs)
    wrapper.model_admin = self
    return update_wrapper(wrapper, view)

  def get_urls(self):
    urlpatterns = super(RemitoAdmin, self).get_urls()
    return urlpatterns


# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)
# admin.site.register(Pedido, PedidoAdmin)
# admin.site.register(Remito, RemitoAdmin)
