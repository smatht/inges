from django.contrib import admin

# Register your models here.
from models import TipoCaja, MovCaja, TipoMovCaja

@admin.register(MovCaja)
class MovCajaAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'obra', 'importe', 'tipoMovCaja', 'descripcion')
    list_filter = ('caja__destino',)

    def obra(self, obj):
        return obj.caja.destino

admin.site.register(TipoCaja)
admin.site.register(TipoMovCaja)
