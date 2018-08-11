from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

from .views import RecetasView, RecetaDetailView

app_name = 'recetas'
urlpatterns = [
    url(r'^$', RecetasView.as_view(), name='view'),
    url(r'^(?P<slug>[-\w]+)/$', RecetaDetailView.as_view(), name='detail'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
