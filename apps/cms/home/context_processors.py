from apps.cms.recetas.models import Receta


def recetas_slider_home(request):
    return {
        'recetas_slider_home': Receta.objects.filter(
            slider_display=True,
            publicado=True
        )
    }
