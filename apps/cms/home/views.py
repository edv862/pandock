from django.shortcuts import render
from django.views.generic import ListView

from .models import Slider, Noticia


class HomeView(ListView):
    template_name = 'home.html'
    model = Slider

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['slider'] = Slider.objects.all().order_by('posicion')[0:3]
        context['noticias'] = Noticia.objects.all().order_by('posicion')[0:3]

        return context
