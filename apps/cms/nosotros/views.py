from django.shortcuts import render
from django.views.generic import ListView
from .models import Nosotros


class NosotrosView(ListView):
    template_name = 'nosotros.html'
    model = Nosotros

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        try:
            context['nosotros'] = Nosotros.objects.all().order_by('-id')[0]
        except Exception as e:
            context['nosotros'] = None

        return context
