from django.contrib import admin
from .models import TipoSecuestro, Secuestro

# Register your models here
class SecuestroAdmin(admin.ModelAdmin):
    pass

admin.site.register(TipoSecuestro,admin.ModelAdmin)
admin.site.register(Secuestro,admin.ModelAdmin)
