from django.db import models
from model_utils.models import TimeStampedModel


class Ubicacion(TimeStampedModel):
    estado = models.CharField(max_length=100)
    direccion = models.TextField()
    coordenadas = models.URLField()

    class Meta:
        verbose_name_plural = "Ubicaciones"
