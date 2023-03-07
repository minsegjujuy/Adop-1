from django.contrib import admin
from .models import Procedimiento, ProcedimientoPersona, TipoProcedimiento, DetalleProcedimiento

# Register your models here.
class ProcedimientoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Procedimiento,admin.ModelAdmin)
admin.site.register(ProcedimientoPersona,admin.ModelAdmin)
admin.site.register(TipoProcedimiento,admin.ModelAdmin)
admin.site.register(DetalleProcedimiento,admin.ModelAdmin)
