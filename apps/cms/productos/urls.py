from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings

from .views import ProductosView

app_name = 'productos'
urlpatterns = [
    url(r'^$', ProductosView.as_view(), name='view'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
