from django.contrib import admin
from .models import Vigilancia, TurnosVigilancia, PersonalVigilancia

# Register your models here.
class VigilanciaAdmin(admin.ModelAdmin):
    pass

admin.site.register(Vigilancia,admin.ModelAdmin)
admin.site.register(TurnosVigilancia,admin.ModelAdmin)
admin.site.register(PersonalVigilancia,admin.ModelAdmin)
