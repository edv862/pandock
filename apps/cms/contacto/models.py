from django.db import models


class Departamento(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()

    class Meta:
        ordering = ['nombre', ]

    def __str__(self):
        return self.nombre
