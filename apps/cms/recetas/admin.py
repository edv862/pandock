from django.contrib import admin
from .models import Receta, Categoria


class RecetaAdmin(admin.ModelAdmin):
    empty_value_display = '-Seleccione-'
    list_display = ('titulo', 'categoria', 'complejidad')
    exclude = ('slug', )


admin.site.register(Categoria)
admin.site.register(Receta, RecetaAdmin)
