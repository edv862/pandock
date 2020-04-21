from django.contrib import admin

from .models import Slider, Noticia


class SliderAdmin(admin.ModelAdmin):
	list_display = ('posicion', 'publicado',)


class NoticiaAdmin(admin.ModelAdmin):
	list_display = ('titulo', 'posicion', 'publicado',)


admin.site.register(Slider, SliderAdmin)
admin.site.register(Noticia, NoticiaAdmin)
