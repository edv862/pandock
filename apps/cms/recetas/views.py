from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.generic import ListView, DetailView
from .models import Receta, Categoria


class RecetasView(ListView):
    template_name = 'recetas.html'
    model = Receta

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['recetas'] = Receta.objects.all()
        context['categorias'] = Categoria.objects.all()

        return context


class RecetaDetailView(DetailView):
    template_name = 'recetas.html'
    model = Receta

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        slug = self.kwargs['slug']

        context['recetas'] = Receta.objects.all()
        context['receta_detail'] = get_object_or_404(Receta, slug=slug)
        context['categorias'] = Categoria.objects.all()

        return context
