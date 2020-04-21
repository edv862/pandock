from django.db import models


class Departamento(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(blank=True, null=True)

    class Meta:
        ordering = ['nombre', ]

    def __str__(self):
        return repr(self.nombre.encode('utf-8'))


class Ubicacion(models.Model):
	nombre = models.CharField(max_length=100)

	class Meta:
		ordering = ['nombre',]

	def __str__(self):
		return str(self.nombre)
