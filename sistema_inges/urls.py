from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

import compras
import fondos
from compras.views import ComprasViewSet
from fondos.views import ReporteCajaView
from stock.views import PROViewSet

admin.autodiscover()

from facturacion.views import FRViewSet
from rest_framework import routers
router = routers.DefaultRouter()

import facturacion.urls
from fondos_externos.views import save_cuenta, get_registros

router.register(r'links', FRViewSet)
router.register(r'precios', PROViewSet)
router.register(r'compras', ComprasViewSet)

urlpatterns = patterns('',
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^administracion/', include(admin.site.urls)),
    (r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^tellme/', include("tellme.urls")),
    url(r'^', include(facturacion.urls)),
    url(r'^reportes/analisis_corporativo$', compras.views.InformeAnalisisCorporativo, name='analisis_corporativo'),
    url(r'^reportes/exclusivos_laruta$', compras.views.ExclusivoLaRuta, name='exclusivos_laruta'),
    url(r'^reportes/reporte_caja$', fondos.views.ReporteCajaView, name='reporte_caja'),
    url(r'^cuentas-wallet/', save_cuenta),
    url(r'^registros-wallet/(\d+)/', get_registros)


    # Examples:
    # url(r'^$', 'sistema_inges.views.home', name='home'),
    # url(r'^sistema_inges/', include('sistema_inges.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
