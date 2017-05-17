from django.conf.urls import url
from django.contrib import admin

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
  list_display = ('fecha', 'registro', 'proveedor', 'destino', 'account_actions')
  exclude = ('remitente', )
  inlines = [ORDetInline]
  actions = [export_OR_as_pdf]
  fieldsets = [
    (None, {'fields': ['registro', 'fecha', 'proveedor','destino']}),
    ('Orden de retiro', {
      'description': 'Para extender una orden de retiro complete este campo',
      'fields': ['se_autoriza', 'firmante']}),
    ]

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

  def process_deposit(self, request, account_id, *args, **kwargs):
    qs = PedidoCabecera.objects.get(pk=account_id)
    return export_OR_as_pdf(self, request, qs)

  def get_urls(self):
    urls = super(ORCabAdmin, self).get_urls()
    custom_urls = [
      url(
        r'^(?P<account_id>.+)/deposit/$',
        self.admin_site.admin_view(self.process_deposit),
        name='account-deposit',
      ),
    ]
    return custom_urls + urls


class RemitoDetalleInline(admin.TabularInline):
  form = PedidoDetalleForm
  # template = 'admin/edit_inline/stacked.html'
  model = RemitoDetalle
  extra = 5


class RemitoAdmin(admin.ModelAdmin):
  form = RemitoForm
  inlines = [RemitoDetalleInline]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(PedidoCabecera, ORCabAdmin)
admin.site.register(RemitoCabecera, RemitoAdmin)