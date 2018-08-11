from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings

from .views import NosotrosView

app_name = 'nosotros'
urlpatterns = [
    url(r'^$', NosotrosView.as_view(), name='view'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
