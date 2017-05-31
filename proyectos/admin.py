from django.contrib import admin

from proyectos.forms import ObrasForm
from proyectos.models import Obra

class ObraAdmin(admin.ModelAdmin):
  form = ObrasForm


admin.site.register(Obra, ObraAdmin)
