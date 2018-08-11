# -*- coding: utf-8 -*-
from django.db import models
from model_utils.models import TimeStampedModel


class Nosotros(TimeStampedModel):
    columna_uno = models.TextField()
    columna_dos = models.TextField()

    class Meta:
        verbose_name = 'Nosotros'
        verbose_name_plural = 'Nosotros'

    def __str__(self):
        return "Nosotros información"
