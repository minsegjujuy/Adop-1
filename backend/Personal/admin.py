from django.contrib import admin
from .models import Categoria, Funcionario, Personal, Jerarquia, SubCategoria


# # Register your models here.
class PersonalAdmin(admin.ModelAdmin):
    pass


admin.site.register(Personal, admin.ModelAdmin)
admin.site.register(Jerarquia, admin.ModelAdmin)
admin.site.register(Categoria, admin.ModelAdmin)
admin.site.register(SubCategoria, admin.ModelAdmin)
admin.site.register(Funcionario, admin.ModelAdmin)
