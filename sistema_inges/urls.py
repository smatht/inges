from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

from stock.views import PROViewSet

admin.autodiscover()

from facturacion.views import FRViewSet
from rest_framework import routers
router = routers.DefaultRouter()

import facturacion.urls
from fondos_externos.views import save_cuenta
router.register(r'links', FRViewSet)
router.register(r'precios', PROViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^administracion/', include(admin.site.urls)),
    # url(r'^logout/$', include('django.contrib.auth.views.logout')),
    url(r'^tellme/', include("tellme.urls")),
    url(r'^', include(facturacion.urls)),
    url(r'^cuentas-wallet/', save_cuenta)
]
    # + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
    #           + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
