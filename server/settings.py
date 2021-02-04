"""
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = os.environ.get("SECRET_KEY", "SOME_NOT-TOP_SECRET")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DEBUG", True)

if DEBUG:
    ALLOWED_HOSTS = []
else:
    ALLOWED_HOSTS = ['appboxo-djtodo.herokuapp.com','127.0.0.1', '0.0.0.0']


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # THIRD-PARTY MODULES
    'rest_framework',

    # LOCAL APPS
    'todo',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'server.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'server.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

"""
Local development database settings. 
"""
DATABASES = {
    'default': {
        'ENGINE': "django.db.backends.postgresql", #os.environ.get('DB_ENGINE', 'django.db.backends.sqlite3'),
        'NAME': "postgres", #os.environ.get('DB_DATABASE_NAME', os.path.join(BASE_DIR, 'db.sqlite3')),
        'USER': "postgres", #os.environ.get('DB_USERNAME', 'user'),
        'PASSWORD': "postgres", #os.environ.get('DB_PASSWORD', 'password'),
        'HOST': "db", #os.environ.get('DB_HOST', 'localhost'),
        'PORT': 5432, #os.environ.get('DB_PORT', '5432'),
    }
}
"""
Heroku database settings. Uncomment when you want to use it.
Put this below the DATABASE={ ... } configuration.
"""
# import dj_database_url
# db_from_env = dj_database_url.config()
# DATABASES['default'].update(db_from_env)
# DATABASES['default']['CONN_MAX_AGE'] = 500


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


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/


STATIC_URL = '/static/'
STATIC_ROOT = '/static'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    )
}
#CSRF_TRUSTED_ORIGINS = ['127.0.0.1'] # in development mode

# CACHES = {
#     "default": {
#         "BACKEND": 'django_redis.cache.RedisCache',
#         "LOCATION": os.environ.get("REDIS_LOCATION"), # 'redis://<username if exists>:<password>@<host_end_point>:<post>/<db_index (best is 0)>'
#         "OPTIONS": {
#             "CLIENT_CLASS": 'django_redis.client.DefaultClient'
#         },
#         "KEY_PREFIX": "app_box"
#     }
# }

CACHE_TTL = 30