from django.db import models
from django.core.validators import RegexValidator, MinValueValidator
from model_utils.models import TimeStampedModel


class Ubicacion(TimeStampedModel):
    estado = models.CharField(max_length=100)
    razon_social = models.CharField(max_length=200)
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
    mapa_url = models.URLField(max_length=1000)

    x_coord = models.PositiveIntegerField(
        "Coordenada X",
        validators=[MinValueValidator(1)],
        null=True,
        blank=True,
    )
    y_coord = models.PositiveIntegerField(
        "Coordenada X",
        validators=[MinValueValidator(1)],
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.estado

    class Meta:
        verbose_name_plural = "Ubicaciones"
        verbose_name = "Ubicaciones"
