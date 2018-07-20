from django.conf.urls import url, include

from .views import UbicacionView

app_name = 'donde_estamos'
urlpatterns = [
    url(r'^$', UbicacionView.as_view(), name='view'),
]