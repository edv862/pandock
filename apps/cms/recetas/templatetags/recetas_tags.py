from django import template
from ..models import Receta

register = template.Library()


@register.simple_tag
def receta_by_category(category):
    return Receta.objects.filter(categoria=category)
