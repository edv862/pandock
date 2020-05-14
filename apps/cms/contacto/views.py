#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.core.mail import BadHeaderError, EmailMessage
from django.views.generic import TemplateView, ListView

from .forms import ContactoForm, ContactoRecursosHumanosForm
from .models import Departamento, Ubicacion


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


def send_email_rh(request):
    nombre = request.POST.get('nombre', '')
    correo = request.POST.get('correo', '')
    ubicacion = request.POST.get('ubicacion', '')
    dpto = request.POST.get('departamento', '')
    mensaje = request.POST.get('mensaje', '')
    archivo = request.FILES.get('archivo', '')

    dep = get_object_or_404(Departamento, id=dpto)

    if nombre and correo and ubicacion and dpto and mensaje and archivo:
        estado = Ubicacion.objects.get(id=ubicacion)

        message = nombre + ' ha enviado un correo a traves del sitio web de pandock.\n'
        message += "Departamento " + dep.nombre + ".\n"
        message += mensaje + ".\n"
        message += "Contacto de " + nombre + " - " + correo + "\n"
        message += "Ubicación: " + ubicacion + "\n"

        email = EmailMessage(
            subject="Recursos Humanos - Web Email.",
            body=message,
            from_email='pagina_web@pandock.com',
            to=[dep.correo]
        )

        email.attach('curriculum.pdf', archivo.file.getvalue(), 'application/pdf')
        email.send()

        messages.success(request, "Correo enviado.")
        return HttpResponseRedirect(reverse_lazy('contacto:view'))
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        messages.error(request, "Ocurrio un error enviando el correo, revise el formulario.")
        return HttpResponseRedirect(reverse_lazy('contacto:view'))


def send_email_compras_importaciones(request):
    nombre = request.POST.get('nombre', '')
    correo = request.POST.get('correo', '')
    ubicacion = request.POST.get('ubicacion', '')
    mensaje = request.POST.get('mensaje', '')

    if nombre and ubicacion and correo and mensaje:
        estado = Ubicacion.objects.get(id=ubicacion)

        message = nombre + ' ha enviado un correo a traves del sitio web de pandock.\n'
        message += mensaje + ".\n"
        message += "Contacto de " + nombre + " - " + correo + "\n"
        message += "Ubicación: " + ubicacion + "\n"

        email = EmailMessage(
            subject="Compras e Importaciones - Web Email.",
            body=message,
            from_email='pagina_web@pandock.com',
            to=["compras@pandock.com"]
        )
        email.send()

        messages.success(request, "Correo enviado.")
        return HttpResponseRedirect(reverse_lazy('contacto:view'))
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        messages.error(request, "Ocurrio un error enviando el correo, revise el formulario.")
        return HttpResponseRedirect(reverse_lazy('contacto:view'))


def send_email_atencion(request):
    nombre = request.POST.get('nombre', '')
    correo = request.POST.get('correo', '')
    ubicacion = request.POST.get('ubicacion', '')
    mensaje = request.POST.get('mensaje', '')

    if nombre and ubicacion and correo and mensaje:
        estado = Ubicacion.objects.get(id=ubicacion)

        message = nombre + ' ha enviado un correo a traves del sitio web de pandock.\n'
        message += mensaje + ".\n"
        message += "Contacto de " + nombre + " - " + correo + "\n"
        message += "Ubicación: " + ubicacion + "\n"

        email = EmailMessage(
            subject="Atencion al Cliente - Web Email.",
            body=message,
            from_email='pagina_web@pandock.com',
            to=["atencion_clientes@pandock.com"]
        )
        email.send()

        messages.success(request, "Correo enviado.")
        return HttpResponseRedirect(reverse_lazy('contacto:view'))
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        messages.error(request, "Ocurrio un error enviando el correo, revise el formulario.")
        return HttpResponseRedirect(reverse_lazy('contacto:view'))
