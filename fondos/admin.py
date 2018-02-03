from django.contrib import admin

# Register your models here.
from models import TipoCaja, MovCaja, TipoMovCaja

admin.site.register(TipoCaja)
admin.site.register(MovCaja)
admin.site.register(TipoMovCaja)
