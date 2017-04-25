from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.inicio, name='inicio'),
    url(r'^facturas_recibidas/$', views.facturas_recibidas, name='facturas-recibidas'),
    url(r'^facturas_recibidas/(\d+)/(\d+)$', views.facturas_recibidas, name='facturas'),
    # url(r'^facturas_recibidas/add/$', 'facturacion.views.addFR', name='add'),
    url(r'^facturacion/informes/$', views.informesFacturacion, name='informe'),
    url(r'^xls/$', views.xls, name='export'),
]