from django.shortcuts import render
from django.views.generic import FormView, TemplateView


class ContactoView(TemplateView):
    template_name = 'contacto.html'
