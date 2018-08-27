from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from .models import Receta, Categoria, RecetasSlider


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'orden', )


class RecetaAdmin(admin.ModelAdmin):
    empty_value_display = '-Seleccione-'
    list_display = ('titulo', 'titulo_resumido', 'categoria', 'complejidad', 'publicado', 'slider_display', )
    list_editable = ('publicado', 'slider_display', )
    exclude = ('slug', )

    def publicado(self, obj):
        return obj.publicado
    publicado.boolean = True

    def slider_display(self, obj):
        return obj.slider_display
    slider_display.boolean = True
    slider_display.short_description = 'Mostrar en slider home'


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Receta, RecetaAdmin)
admin.site.register(RecetasSlider)
