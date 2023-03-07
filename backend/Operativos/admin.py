from django.contrib import admin
from .models import Operativo, OperativoPersonal

# # Register your models here.
class OperativoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Operativo,admin.ModelAdmin)
admin.site.register(OperativoPersonal,admin.ModelAdmin)
