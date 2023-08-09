from django.contrib import admin

from .models import Ente


# Register your models here.
class EnteAdmins(admin.ModelAdmin):
    pass


admin.site.register(Ente, admin.ModelAdmin)
