from django.contrib import admin
from .models import Servicio, TipoServicio, TipoRecurso


# Register your models here.
class ServicioAdmin(admin.ModelAdmin):
    pass


admin.site.register(TipoServicio, admin.ModelAdmin)
admin.site.register(Servicio, admin.ModelAdmin)
admin.site.register(TipoRecurso, admin.ModelAdmin)
