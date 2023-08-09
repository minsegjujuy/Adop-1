from django.contrib import admin
from .models import Dependencia, Inspectora, UnidadRegional, DependenciaOperativos


# Register your models here.
class DependennciasAdmin(admin.ModelAdmin):
    pass


admin.site.register(Dependencia, admin.ModelAdmin)
admin.site.register(Inspectora, admin.ModelAdmin)
admin.site.register(UnidadRegional, admin.ModelAdmin)
admin.site.register(DependenciaOperativos, admin.ModelAdmin)
