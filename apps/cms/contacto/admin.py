from django.contrib import admin

from .models import Departamento, Ubicacion


class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'correo')


class UbicacionAdmin(admin.ModelAdmin):
	list_display = ('nombre',)


admin.site.register(Departamento, DepartamentoAdmin)
admin.site.register(Ubicacion, UbicacionAdmin)
