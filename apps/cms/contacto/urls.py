from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings

from .views import ContactoView

app_name = 'contacto'
urlpatterns = [
    url(r'^$', ContactoView.as_view(), name='view'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
