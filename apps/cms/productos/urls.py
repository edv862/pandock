from django.conf.urls import url, include

from .views import ProductosView

app_name = 'productos'
urlpatterns = [
    url(r'^$', ProductosView.as_view(), name='view'),
]