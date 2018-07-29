import io
import os
import sys
from django.db import models
from model_utils.models import TimeStampedModel
from django.core.exceptions import ValidationError

from django.core.files import File
from django.core.files.uploadedfile import InMemoryUploadedFile

from .excel2pdf import create_pdf
from fpdf import FPDF

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
        return str(self.pk) + " - " + self.titulo

    def clean(self):        
        try:
            excel = self.archivo.file #the file in Memory
            # this prints <class 'django.core.files.uploadedfile.InMemoryUploadedFile'>
            # print(excel.__class__)
            new_pdf = create_pdf(excel, self.titulo)
            path = self.set_pathfile(self.titulo)
            # new_pdf_io = io.BytesIO(str.encode(new_pdf.output('S')))x
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
            """
            pdf.output(path,"F")
            self.archivo.storage.save(path)
            print("----------------Right here -----------------")
            print(self.archivo)
            """
        except ValueError:
            pass

    def set_pathfile(self,titulo):
        path = 'media/productos/pdf/'
        pdf_title = titulo.replace(" ","_").lower() + '.pdf'
        return path + pdf_title