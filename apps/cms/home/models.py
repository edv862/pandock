#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
from django.core.validators import MinValueValidator
from model_utils.models import TimeStampedModel


class Slider(TimeStampedModel):
    image = models.ImageField(
        upload_to='home/slider'
    )
    posicion = models.PositiveIntegerField(
        validators=[MinValueValidator(1)],
    )
    publicado = models.BooleanField(
        default=True,
    )

    def __str__(self):
        return "Imagen Slider " + str(self.posicion)


class Noticia(TimeStampedModel):
    titulo = models.CharField(max_length=100)
    image = models.ImageField(
        upload_to='home/noticias',
        blank=True,
        null=True
    )
    texto = models.TextField()

    publicado = models.BooleanField(
        default=True,
    )
    posicion = models.PositiveIntegerField(
        validators=[MinValueValidator(1)],
    )

    def __str__(self):
        return str(self.posicion) + " - " + self.titulo
