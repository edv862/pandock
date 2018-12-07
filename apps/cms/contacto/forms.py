#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from antispam.honeypot.forms import HoneypotField
from antispam.captcha.forms import ReCAPTCHA


class ContactoForm(forms.Form):
    nombre = forms.CharField()
    correo = forms.EmailField()
    mensaje = forms.CharField(widget=forms.Textarea({'rows': 6}))
    spam_honeypot_field = HoneypotField()
    captcha = ReCAPTCHA()


class ContactoRecursosHumanosForm(forms.Form):
    nombre = forms.CharField()
    correo = forms.EmailField()
    mensaje = forms.CharField(widget=forms.Textarea)
    departamento = forms.ChoiceField()
    archivo = forms.FileField()
    spam_honeypot_field = HoneypotField()
    captcha = ReCAPTCHA()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        choices = [("", "Departamento")]

        for choice in kwargs['initial']['departamento']:
            choices += [(choice.id, choice.nombre)]

        self.fields["departamento"].choices = choices
