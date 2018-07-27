from django.shortcuts import render

from django.views.generic import ListView
from .models import Ubicacion

class UbicacionView(ListView):
    template_name = "ubicacion.html"
    model = Ubicacion

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['direcciones_mapa'] = Ubicacion.objects.all()
        aux = Ubicacion.objects.all().order_by('estado')
        print(int(len(aux)/2))
        context['direcciones1'] = aux[0: int(len(aux)/2)+1]
        context['direcciones2'] = aux[int(len(aux)/2)+1: len(aux)]


        return context
