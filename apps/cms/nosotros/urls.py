from django.conf.urls import url, include

from .views import NosotrosView

app_name = 'nosotros'
urlpatterns = [
    url(r'^$', NosotrosView.as_view(), name='view'),
]