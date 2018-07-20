from django.db import models

from model_utils import Choices
from model_utils.models import TimeStampedModel


class Slider(TimeStampedModel):
    POSICION = Choices('1', '2', '3')

    image = models.ImageField(
        upload_to='home/slider'
    )
    posicion = models.CharField(
        choices=POSICION,
        max_length=2
    )

    def __str__(self):
        return "Imagen Slider " + self.posicion


class Noticia(TimeStampedModel):
    POSICION = Choices('1', '2', '3')

    titulo = models.CharField(max_length=100)
    image = models.ImageField(
        upload_to='home/noticias',
        blank=True,
        null=True
    )
    texto = models.TextField()

    posicion = models.CharField(
        choices=POSICION,
        max_length=2
    )

    def __str__(self):
        return self.posicion + " - " + self.titulo
