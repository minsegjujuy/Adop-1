from django.contrib import admin

from Archivo.models import Documento

# Register your models here.
class ArchivoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Documento, admin.ModelAdmin)