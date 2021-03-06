#encoding:utf-8
# Django settings for sistema_inges project.
#
# export INGESDB_NAME=df4sco1u608bra
# export INGESDB_HOST=ec2-107-21-236-219.compute-1.amazonaws.com
# export INGESDB_PORT=5432
# export INGESDB_USER=opxavbxjahzkut
# export INGESDB_PASSWORD=5c8cd1ae416ad7593efae3ded70d6db194cc40d629cc531aff51b959dedb30f7

import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Matias G. Sticchi', 'matgs656@gmail.com'),
    # ('Your Name', 'your_email@example.com'),
)

# TELLME_FEEDBACK_EMAIL = 'matgs656@gmail.com'
# Parse database configuration from $DATABASE_URL

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

MANAGERS = ADMINS

# Acceso a linea de comando de la base
# heroku pg:psql --app sistema-inges HEROKU_POSTGRESQL_GREEN

# SETTING DATA BASE
# Configurar las variables de entorno en /etc/profile
NAME = os.environ.get('INGESDB_NAME', 'df4sco1u608bra')
HOST = os.environ.get('INGESDB_HOST', 'ec2-107-21-236-219.compute-1.amazonaws.com')
PORT = os.environ.get('INGESDB_PORT', 5432)
USER = os.environ.get('INGESDB_USER', 'opxavbxjahzkut')
PASSWORD = os.environ.get('INGESDB_PASSWORD', '5c8cd1ae416ad7593efae3ded70d6db194cc40d629cc531aff51b959dedb30f7')
DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': NAME,
    'HOST': HOST,
    'PORT': PORT,
    'USER': USER,
    'PASSWORD': PASSWORD
  }
}
# Acceso a linea de comando de la base
# heroku pg:psql --app sistema-inges HEROKU_POSTGRESQL_RED

RUTA_PROYECTO = os.path.dirname(os.path.realpath(__file__))

LOGIN_URL = '/accounts/login/'

#LOGIN_REDIRECT_URL = 'accounts/login/'

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['*']

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Argentina/Buenos_Aires'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'es-AR'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = os.path.join(RUTA_PROYECTO, 'static')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

# Static asset configuration
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
# STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
STATIC_ROOT = 'staticfiles'

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    os.path.join(RUTA_PROYECTO, 'static'),
    # os.path.join(BASE_DIR, 'static'),
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
# 'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '$5o+=*d#pa=3z2%*vun0@6h_))&2r!^1u@onv7i1!@b))vl&g&'
# Token for BudgetBakers Wallet
WALLET_KEY = '5a3709ce-acfb-49fb-8b60-b1b9e55ffb51'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
# 'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware', #(deprecated)
    # 'django.contrib.auth.middleware.SessionAuthenticationMiddleware'
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'sistema_inges.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'sistema_inges.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(RUTA_PROYECTO,'templates'),
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    'django.contrib.admindocs',
    'suitlocale',
    'suit',
    'facturacion',
    'common',
    'rest_framework',
    'tellme',
    'proyectos',
    # 'pedidos',
    'compras',
    'stock',
    'mantenimiento',
    'fondos',
    'daterange_filter',
    'fondos_externos',
)
# Any global settings for a REST framework API are kept in a single configuration dictionary named REST_FRAMEWORK.
# Start off by adding the following to your settings.py module:
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
SUIT_CONFIG = {
    # header
    'ADMIN_NAME': 'SISTEMA INGES',
    'VERSION': 'v1.0',
    'HEADER_DATE_FORMAT': 'l, j. F Y',
    'HEADER_TIME_FORMAT': 'H:i',

    # forms
    'SHOW_REQUIRED_ASTERISK': True, # Default True
    # 'CONFIRM_UNSAVED_CHANGES': True, # Default True

    # menu
    # 'SEARCH_URL': '/admin/auth/user/',
    # 'MENU_ICONS': {
    # 'sites': 'icon-leaf',
    # 'auth': 'icon-lock',
    # },
    'MENU_OPEN_FIRST_CHILD': True,  # Default True
    # 'MENU_EXCLUDE': ('auth.group',),
    'MENU': (
        {'app': 'mantenimiento', 'models': (
            {'label': 'Ajustes', 'url': '/administracion/mantenimiento/configuracion/1/', 'permissions': 'mantenimiento.add_configuracion'},
            {'model': 'facturacion.registro', 'label': 'Empresas', 'permissions': 'facturacion.add_registro'},
            {'model': 'mantenimiento.impuesto', 'label': 'Impuestos', 'permissions': 'mantenimiento.add_impuesto'},
            {'model': 'mantenimiento.tiposdoc', 'label': 'Documentos', 'permissions': 'mantenimiento.add_tiposdoc'},
            {'model': 'proyectos.obra', 'label': 'Obras', 'permissions': 'proyectos.add_obra'},
        )},
        {'app': 'facturacion', 'models': (
            {'model': 'facturacion.cliente', 'label': 'Clientes', 'permissions': 'facturacion.add_cliente'},
            {'model': 'facturacion.emision_factura', 'label': 'Emitir factura', 'permissions': 'facturacion.add_emision_factura'},
        )},
        {'app': 'compras', 'models': (
            {'model': 'facturacion.proveedor', 'label': 'Proveedores', 'permissions': 'facturacion.add_proveedor'},
            {'model': 'compras.compra', 'label': 'Documentos de compra', 'permissions': 'compras.add_compra'},
            {'model': 'compras.pedido', 'label': 'Ordenes de compra', 'permissions': 'compras.add_pedido'},
            {'model': 'compras.remito', 'label': 'Remitos de compra', 'permissions': 'compras.add_remito'},
        )},
        {'app': 'fondos', 'models': (
            {'model': 'fondos.tipocaja', 'label': 'Tipos de caja', 'permissions': 'fondos.add_tipocaja'},
            {'model': 'fondos.caja', 'label': 'Cajas', 'permissions': 'fondos.add_caja'},
            {'model': 'fondos.movcaja', 'label': 'Movimiento de caja', 'permissions': 'fondos.add_movcaja'},
            {'model': 'fondos.tipomovcaja', 'label': 'Tipo movimiento', 'permissions': 'fondos.add_tipomovcaja'},
            {'model': 'fondos.ordenpago', 'label': 'Orden de pago', 'permissions': 'fondos.add_ordenpago'},
            {'label': 'Reporte de caja', 'icon': 'icon-briefcase', 'url': 'fondos.views.ReporteCajaView', 'permissions': 'facturacion.add_informes'},
        )},
        {'app': 'stock', 'models': (
            {'model': 'stock.producto', 'label': 'Productos', 'permissions': 'stock.add_producto'},
            {'model': 'stock.familia', 'label': 'Familias', 'permissions': 'stock.add_familia'},
            {'model': 'stock.unidades', 'label': 'Unidades', 'permissions': 'stock.add_unidades'},
        )},
        {'label': 'Reportes - Consultas', 'icon': 'icon-briefcase', 'models': (
            {'label': 'Informe compra x venta', 'icon': 'icon-briefcase', 'url': 'facturacion.views.informesFacturacion', 'permissions': 'facturacion.add_informes'},
            {'label': 'Reporte Analisis Corporativo', 'icon': 'icon-briefcase', 'url': 'compras.views.InformeAnalisisCorporativo', 'permissions': 'facturacion.add_informes'},
        )},
        {'label': 'Reportes exclusivos', 'icon': 'icon-briefcase', 'models': (
            {'label': 'La Ruta (consumo mensual)', 'icon': 'icon-briefcase', 'url': 'compras.views.ExclusivoLaRuta', 'permissions': 'facturacion.add_informes'},
        )},
        {'app': 'auth', 'icon':'icon-lock', 'models': ('user', 'group')},
        ),

}
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP
TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
    # 'facturacion.context_processors.ejemplo',
)

FIXTURE_DIRS = (
    os.path.join(RUTA_PROYECTO, 'fixtures'),
)

# MODELS VARS
COND_PAGO = (
        ('CTD', 'Contado'),
        ('CRE', 'Crédito'),
)

# Listado de origenes de datos
ORIGENES_DATOS = (
    (0, 'SISTEMA INGES'),
    (1, 'MOVIL'),
    (2, 'WALLET'),
)

SERIES_COLORS = ['#2f7ed8', '#0d233a', '#8bbc21', '#910000', '#1aadce', '#492970',
		'#f28f43', '#77a1e5', '#c42525', '#a6c96a']