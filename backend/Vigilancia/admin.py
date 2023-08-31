from django.contrib import admin
from .models import (
    Motivo,
    Vigilancia,
    TurnosVigilancia,
    PersonalVigilancia,
    RecursosVigilancia,
)


# Register your models here.
class VigilanciaAdmin(admin.ModelAdmin):
    pass


admin.site.register(Vigilancia, admin.ModelAdmin)
admin.site.register(Motivo, admin.ModelAdmin)
admin.site.register(TurnosVigilancia, admin.ModelAdmin)
admin.site.register(RecursosVigilancia, admin.ModelAdmin)
admin.site.register(PersonalVigilancia, admin.ModelAdmin)
