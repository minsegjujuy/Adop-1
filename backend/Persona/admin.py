from django.contrib import admin
from .models import Persona


# # Register your models here.
class PersonaAdmin(admin.ModelAdmin):
    pass


admin.site.register(Persona, admin.ModelAdmin)
