from django.contrib import admin
from .models import Producto


class ProductoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'imagen', 'tiene_archivo', 'publicado', 'archivo_publicado')

    def tiene_archivo(self, obj):
        if obj.archivo:
            return True
        return False
    tiene_archivo.boolean = True


admin.site.register(Producto, ProductoAdmin)
