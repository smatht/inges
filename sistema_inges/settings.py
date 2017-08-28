#encoding:utf-8
# Django settings for sistema_inges project.

# export INGESDB_NAME=d3vobr4ece5eqg
# export INGESDB_HOST=ec2-54-197-241-82.compute-1.amazonaws.com
# export INGESDB_PORT=5432
# export INGESDB_USER=rvurxlyzmbxmul
# export INGESDB_PASSWORD=D7-2CMosP-26LfwapnlNHTbZ7r

import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Matias G. Sticchi', 'matgs656@gmail.com'),
    # ('Your Name', 'your_email@example.com'),
)

# TELLME_FEEDBACK_EMAIL = 'matgs656@gmail.com'
# Parse database configuration from $DATABASE_URL
import dj_database_url

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

MANAGERS = ADMINS

# Acceso a linea de comando de la base
# heroku pg:psql --app sistema-inges HEROKU_POSTGRESQL_GREEN

# SETTING DATA BASE
# Configurar las variables de entorno en /etc/profile
NAME = os.environ['INGESDB_NAME']
HOST = os.environ['INGESDB_HOST']
PORT = os.environ['INGESDB_PORT'] if os.environ['INGESDB_PORT'] else 5432
USER = os.environ['INGESDB_USER']
PASSWORD = os.environ['INGESDB_PASSWORD']
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
MEDIA_ROOT = os.path.join(RUTA_PROYECTO,'static')

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
    os.path.join(RUTA_PROYECTO,'static'),
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
    'django.contrib.auth.middleware.AuthenticationMiddleware',
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
    'suit',
    'tellme',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    'django.contrib.admindocs',
    'facturacion',
    # 'south',
    'rest_framework',
    'pedidos',
    'compras',
    'proyectos',
    'stock',
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
    'MENU_OPEN_FIRST_CHILD': True, # Default True
    # 'MENU_EXCLUDE': ('auth.group',),
    'MENU': (
        {'label': 'Empresas', 'models': ('facturacion.registro', 'facturacion.cliente', 'facturacion.proveedor')},
        {'app': 'facturacion', 'models': (
            # {'label': 'Emitir factura', 'icon': 'none', 'url': '/facturacion/emision/', 'permissions': 'facturacion.add_informes'},
            {'model': 'facturacion.registro_factura', 'label': 'Registrar factura', 'permissions': 'facturacion.add_registro_factura'},
            {'model': 'facturacion.pago', 'label': 'Pagos', 'permissions': 'facturacion.add_pago'},
            {'model': 'facturacion.emision_factura', 'label': 'Emitir factura', 'permissions': 'facturacion.add_emision_factura'},
            {'label': 'Informe facturacion', 'icon': 'icon-briefcase', 'url': 'facturacion.views.informesFacturacion', 'permissions': 'facturacion.add_informes'},
        )},
        {'app': 'pedidos', 'models': (
            {'model': 'pedidos.pedidocabecera', 'label': 'Pedido', 'permissions': 'pedidos.add_pedidocabecera'},
            {'model': 'pedidos.remitocabecera', 'label': 'Remito', 'permissions': 'pedidos.add_remitocabecera'},
        )},
        {'app': 'compras', 'models': (
            {'model': 'compras.pedido', 'label': 'Pedido', 'permissions': 'compras.add_pedido'},
            {'model': 'compras.remito', 'label': 'Remito', 'permissions': 'compras.add_remito'},
        )},
        {'app': 'stock', 'models': (
            {'model': 'stock.producto', 'label': 'Productos', 'permissions': 'stock.add_producto'},
            {'model': 'stock.familia', 'label': 'Familias', 'permissions': 'stock.add_familia'},
            {'model': 'stock.unidades', 'label': 'Unidades', 'permissions': 'stock.add_unidades'},
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
    'facturacion.context_processors.ejemplo',
)

# Django Suit configuration example

