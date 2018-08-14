from django.contrib import admin

from .models import Ubicacion


class UbicacionAdmin(admin.ModelAdmin):
    list_display = ('estado', 'razon_social', 'tiene_link', )

    def tiene_link(self, obj):
        if obj.mapa_url:
            return True
        return False
    tiene_link.boolean = True


admin.site.register(Ubicacion, UbicacionAdmin)
