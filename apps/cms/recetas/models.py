#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
from django.utils.text import slugify
from django.core.validators import MinValueValidator
from model_utils.models import TimeStampedModel


class RecetasSlider(models.Model):
    imagen = models.ImageField(
        upload_to='receta_slider',
        blank=True,
        null=True
    )

    def __str__(self):
        return "Imagen recetas slider " + str(self.id)


class Categoria(TimeStampedModel):
    nombre = models.CharField(max_length=200)
    orden = models.PositiveIntegerField(
        validators=[MinValueValidator(1)],
        null=False,
        blank=False
    )

    class Meta:
        ordering = ['orden', ]

    def __str__(self):
        return self.nombre


class Receta(TimeStampedModel):
    categoria = models.ForeignKey(
        Categoria,
        related_name='receta',
        on_delete=models.CASCADE
    )
    imagen = models.ImageField(
        upload_to='receta',
        blank=True,
        null=True
    )
    titulo = models.CharField(max_length=200)
    titulo_resumido = models.CharField(
        "Titulo para el tab de receta",
        max_length=18
    )
    complejidad = models.IntegerField(default=1, blank=True, null=True)
    informacion_tecnica = models.TextField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    slug = models.SlugField(max_length=200, unique=True)
    ingredientes = models.TextField(blank=True, null=True)
    preparacion = models.TextField(blank=True, null=True)

    publicado = models.BooleanField(
        default=True,
    )
    slider_display = models.BooleanField(
        'Mostrar en slider home',
        default=False,
    )

    class Meta:
        ordering = ['titulo']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __str__(self):
        return self.titulo

    def _get_unique_slug(self):
        slug = slugify(self.titulo)
        unique_slug = slug
        num = 1
        while Receta.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()

        super().save(*args, **kwargs)
