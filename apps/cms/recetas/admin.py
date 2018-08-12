from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from .models import Receta, Categoria


class RecetaAdmin(admin.ModelAdmin):
    empty_value_display = '-Seleccione-'
    list_display = ('titulo', 'categoria', 'complejidad', 'publicado', )
    list_editable = ('publicado', )
    exclude = ('slug', )

    def publicado(self, obj):
        return obj.publicado
    publicado.boolean = True


admin.site.register(Categoria)
admin.site.register(Receta, RecetaAdmin)
