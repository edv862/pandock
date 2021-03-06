#!/usr/bin/env python
# -*- coding: utf-8 -*-
import io
import sys
import datetime
from django.db import models
from model_utils.models import TimeStampedModel
from django.core.files.uploadedfile import InMemoryUploadedFile

from .excel2pdf import create_pdf


class Producto(TimeStampedModel):
    __file = ""
    DEFAULT_IMG = '../assets/img/logo.png'

    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    imagen = models.ImageField(
        "Imagen (logo por default)",
        upload_to='productos/producto',
        default=DEFAULT_IMG,
        blank=True
    )
    archivo = models.FileField(
        upload_to='productos/pdf',
        blank=True,
        null=True,
    )
    publicado = models.BooleanField(
        default=True,
    )
    archivo_publicado = models.BooleanField(
        default=True
    )

    class Meta:
        ordering = ['titulo', ]

    def __str__(self):
        return self.titulo

    def clean(self):

        if not self.imagen:
            self.imagen = self.DEFAULT_IMG

        try:
            excel = self.archivo.file
            new_pdf = create_pdf(excel, self.titulo)

            if new_pdf:
                path = self.set_pathfile(self.titulo)
                new_pdf_io = io.BytesIO(new_pdf.output(dest='S').encode('latin-1'))

                tmp_file = InMemoryUploadedFile(
                    new_pdf_io,
                    path,
                    path,
                    'application/pdf',
                    sys.getsizeof(new_pdf_io),
                    None
                )
                self.archivo = tmp_file
        except ValueError:
            pass

    def set_pathfile(self, titulo):
        path = 'media/productos/pdf/'
        now = datetime.datetime.now()
        date = '_' + str(now.day) + '_' + str(now.month) + '_' + str(now.year)
        pdf_title = titulo.replace(" ", "_").lower() + date + '.pdf'
        return path + pdf_title
