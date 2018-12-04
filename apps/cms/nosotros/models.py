#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
from model_utils.models import TimeStampedModel


class Nosotros(TimeStampedModel):
    descripcion_columna1 = models.TextField()
    descripcion_columna2 = models.TextField()

    class Meta:
        verbose_name = 'Nosotros'
        verbose_name_plural = 'Nosotros'

    def __str__(self):
        return "Nosotros información"
