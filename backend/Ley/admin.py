from django.contrib import admin
from .models import Ley, Articulo, Inciso


# Register your models here.
class LeyAdmin(admin.ModelAdmin):
    pass


admin.site.register(Ley, admin.ModelAdmin)
admin.site.register(Articulo, admin.ModelAdmin)
admin.site.register(Inciso, admin.ModelAdmin)
