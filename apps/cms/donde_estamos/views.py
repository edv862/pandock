from django.shortcuts import render

from django.views.generic import TemplateView


class UbicacionView(TemplateView):
    template_name = "ubicacion.html"
    context_object_name = "ubicacion"
