#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.views.generic import ListView, DetailView
from .models import Receta, Categoria, RecetasSlider


class RecetasView(ListView):
    template_name = 'recetas.html'
    model = Receta

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['recetas'] = Receta.objects.all()
        context['categorias'] = Categoria.objects.all()
        context['recetas_sliders'] = RecetasSlider.objects.all()

        return context


class RecetaDetailView(DetailView):
    template_name = 'recetas.html'
    model = Receta

    def get(self, request, *args, **kwargs):
        receta = get_object_or_404(Receta, slug=self.kwargs['slug'])
        print(self.request.user.is_superuser)

        if not(self.request.user.is_superuser or receta.publicado):
            return HttpResponse('Unauthorized', status=401)
        else:
            return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        slug = self.kwargs['slug']

        context['recetas'] = Receta.objects.all()
        context['receta_detail'] = get_object_or_404(Receta, slug=slug)
        context['categorias'] = Categoria.objects.all()

        return context
