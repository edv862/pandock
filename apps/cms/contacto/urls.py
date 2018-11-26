from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings

from .views import (
    ContactoView, send_email_rh,
    send_email_compras_importaciones, send_email_atencion
)

app_name = 'contacto'
urlpatterns = [
    url(r'^$', ContactoView.as_view(), name='view'),
    url(r'^email_rh/$', send_email_rh, name='email_rh'),
    url(r'^email_compras/$', send_email_compras_importaciones, name='email_compras'),
    url(r'^email_atencion/$', send_email_atencion, name='email_atencion'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
