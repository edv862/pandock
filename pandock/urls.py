"""pandock URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^', include('apps.cms.home.urls', namespace='home')),
    url(r'^nosotros/', include('apps.cms.nosotros.urls', namespace='nosotros')),
    url(r'^productos/', include('apps.cms.productos.urls', namespace='productos')),
    url(r'^recetas/', include('apps.cms.recetas.urls', namespace='recetas')),
    url(r'^sedes/', include('apps.cms.donde_estamos.urls', namespace='donde_estamos')),
    url(r'^contacto/', include('apps.cms.contacto.urls', namespace='contacto')),
    url(r'^admin/', admin.site.urls),
    url(r'^djga/', include('google_analytics.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
