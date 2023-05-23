from django.contrib import admin
from .models import Personal,Jerarquia

# # Register your models here.
class PersonalAdmin(admin.ModelAdmin):
    pass

admin.site.register(Personal,admin.ModelAdmin)
admin.site.register(Jerarquia,admin.ModelAdmin)