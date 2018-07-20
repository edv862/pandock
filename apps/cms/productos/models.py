from django.db import models
from model_utils.models import TimeStampedModel


class Producto(TimeStampedModel):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    imagen = models.ImageField(
        upload_to='productos/producto',
        blank=True,
        null=True,
    )
    archivo = models.FileField(
        upload_to='productos/pdf',
        blank=True,
        null=True,
    )

    def __str__(self):
        return str(self.id) + " - " + self.titulo
