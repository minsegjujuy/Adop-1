from django.contrib import admin
from .models import Personal

# # Register your models here.
class PersonalAdmin(admin.ModelAdmin):
    pass

admin.site.register(Personal,admin.ModelAdmin)
