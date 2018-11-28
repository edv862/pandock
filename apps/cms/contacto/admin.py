from django.contrib import admin

from .models import Departamento


class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('nombre', )


admin.site.register(Departamento, DepartamentoAdmin)
