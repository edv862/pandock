#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.views.generic import TemplateView

from .forms import ContactoForm, ContactoRecursosHumanosForm
from .models import Departamento


class ContactoView(TemplateView):
    template_name = 'contacto.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        departamentos = Departamento.objects.all()

        context['form_recursos_humanos'] = ContactoRecursosHumanosForm(
            initial={'departamento': departamentos}
        )
        context['form_compras'] = ContactoForm()
        context['form_atencion'] = ContactoForm()

        return context
