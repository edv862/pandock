from django.db import models
from django.core.validators import RegexValidator, MinValueValidator
from model_utils.models import TimeStampedModel


class Ubicacion(TimeStampedModel):
    estado = models.CharField(max_length=100)
    rif = models.CharField(max_length=50, blank=True, null=True)
    nit = models.CharField(max_length=50, blank=True, null=True)
    direccion = models.TextField()
    telefono = models.CharField(
        max_length=50,
    )
    fax = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )
    email = models.EmailField(null=True, blank=True)
    mapa_url = models.URLField()

    x_coord = models.PositiveIntegerField(
        "Coordenada X",
        validators=[MinValueValidator(1)]
    )
    y_coord = models.PositiveIntegerField(
        "Coordenada X",
        validators=[MinValueValidator(1)]
    )

    def __str__(self):
        return self.estado

    class Meta:
        verbose_name_plural = "Ubicaciones"
        verbose_name = "Ubicaciones"
