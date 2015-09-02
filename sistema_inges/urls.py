from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from gastos.views import FRViewSet
from rest_framework import routers
router = routers.DefaultRouter()

router.register(r'links', FRViewSet)

urlpatterns = patterns('',
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
	url(r'^$', 'gastos.views.inicio', name='inicio'),
    url(r'^facturas_recibidas/$', 'gastos.views.facturas_recibidas', name='facturas-recibidas'),
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^administracion/', include(admin.site.urls)),
    (r'^logout/$', 'django.contrib.auth.views.logout',
                          {'next_page': '/'}),
    url(r'^facturas_recibidas/(\d+)/(\d+)$', 'gastos.views.facturas_recibidas', name='facturas'),
    url(r'^facturas_recibidas/add/$', 'gastos.views.addFR', name='add'),
    url(r'^facturacion/informes/$', 'gastos.views.informesFacturacion', name='informe'),
    url(r'^xls/$', 'gastos.views.xls', name='export'),



    # Examples:
    # url(r'^$', 'sistema_inges.views.home', name='home'),
    # url(r'^sistema_inges/', include('sistema_inges.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
