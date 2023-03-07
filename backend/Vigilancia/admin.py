from django.contrib import admin
from .models import Vigilancia, DiasVigilancia

# Register your models here.
class VigilanciaAdmin(admin.ModelAdmin):
    pass

admin.site.register(Vigilancia,admin.ModelAdmin)
admin.site.register(DiasVigilancia,admin.ModelAdmin)
