from django.shortcuts import render

from django.views.generic import TemplateView
from .models import Producto


class ProductosView(TemplateView):
    template_name = 'productos.html'
    context_object_name = 'productos'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['productos'] = Producto.objects.all().order_by('id')
        return context
