from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'facturacion.views.index', name='index'),
    url(r'^facturas_recibidas/$', 'facturacion.views.facturas_recibidas', name='facturas-recibidas'),
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    (r'^logout/$', 'django.contrib.auth.views.logout',
                          {'next_page': '/'}),
    url(r'^facturas_recibidas/(\d+)/(\d+)$', 'facturacion.views.facturas_recibidas', name='facturas'),
    url(r'^facturas_recibidas/add/$', 'facturacion.views.addFR', name='add'),

    # Examples:
    # url(r'^$', 'sistema_inges.views.home', name='home'),
    # url(r'^sistema_inges/', include('sistema_inges.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
