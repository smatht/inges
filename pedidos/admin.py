from django.conf.urls import url
from django.contrib import admin

from actions import export_OR_as_pdf, save_then_pdf
from pedidos.forms import PedidoForm
from pedidos.models import PedidoDetalle, PedidoCabecera, ExtendUser

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User


class UserInline(admin.StackedInline):
  model = ExtendUser
  can_delete = False
  verbose_name_plural = 'usuarios'


class UserAdmin(BaseUserAdmin):
  inlines = (UserInline,)

class ORDetInline(admin.TabularInline):
  model = PedidoDetalle
  extra = 1


class ORCabAdmin(admin.ModelAdmin):
  form = PedidoForm
  list_display = ('id', 'fecha', 'registro', 'proveedor', 'destino', 'remitente', 'account_actions')
  exclude = ('remitente', )
  inlines = [ORDetInline]
  actions = [export_OR_as_pdf]

  def save_model(self, request, obj, form, change):
    if getattr(obj, 'remitente', None) is None:
      obj.remitente = request.user
    obj.save()
    # save_then_pdf(request, obj)

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


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(PedidoCabecera, ORCabAdmin)