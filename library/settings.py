import os
import re

from configurations import Configuration, values


class Base(Configuration):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

    SECRET_KEY = values.SecretValue()

    DEBUG = values.BooleanValue(False)

    ALLOWED_HOSTS = values.ListValue(['*'])

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',

        # Third apps
        'rest_framework',
        'drf_yasg',

        # Local apps
        'library.apps.authors.apps.AuthorsConfig',
        'library.apps.base.apps.BaseConfig',
        'library.apps.books.apps.BooksConfig',
    ]

    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'whitenoise.middleware.WhiteNoiseMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]

    ROOT_URLCONF = 'library.urls'

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.path.join(PROJECT_DIR, 'templates')],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]

    WSGI_APPLICATION = 'library.wsgi.application'

    DATABASES = values.DatabaseURLValue('sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3'))

    AUTH_PASSWORD_VALIDATORS = [
        {
            'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
        },
    ]

    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = 'UTC'

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True

    STATIC_URL = '/static/'

    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

    EMAIL = values.EmailURLValue('console://')

    REST_FRAMEWORK = {
        'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
        'DEFAULT_RENDERER_CLASSES': ('rest_framework.renderers.JSONRenderer',),
        'PAGE_SIZE': 10,
    }

    SWAGGER_SETTINGS = {
        'SECURITY_DEFINITIONS': {
            'Basic': {
                'type': 'basic'
            },
            'Bearer': {
                'type': 'apiKey',
                'name': 'Authorization',
                'in': 'header'
            }
        },
        'USE_SESSION_AUTH': False
    }


class Test(Base):
    SECRET_KEY = 'secret_test'
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(Base.BASE_DIR, 'db.sqlite3'),
        }
    }


class Development(Base):
    DOTENV = os.path.join(Base.BASE_DIR, '.development')

    CORS_ORIGIN_ALLOW_ALL = True

    CACHES = values.CacheURLValue('dummy://')

    Base.INSTALLED_APPS.insert(0, 'whitenoise.runserver_nostatic')


class Production(Base):
    CSRF_COOKIE_SECURE = values.BooleanValue(True)

    SESSION_COOKIE_SECURE = values.BooleanValue(True)

    ADMINS = values.SingleNestedTupleValue()

    MANAGERS = ADMINS

    IGNORABLE_404_URLS = [
        re.compile(r'^/apple-touch-icon.*\.png$'),
        re.compile(r'^/favicon.ico$'),
        re.compile(r'^/robots.txt$'),
        re.compile(r'^/phpmyadmin/'),
        re.compile(r'\.(cgi|php|pl)$'),
    ]

    CORS_ORIGIN_WHITELIST = values.ListValue()
