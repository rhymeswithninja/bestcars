import os
from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = (
    "django-insecure-ccow$t"
    "z_=9%dxu4(0%^(z%nx32#"
    "s@(zt9$ih@)5l54yny)wm-0"
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


ALLOWED_HOSTS = [
    'localhost',
    'http://127.0.0.1:8000/',
    (
        'https://chinjaaxiong-8000.theianext-1-labs-prod-'
        'misc-tools-us-east-0.proxy.cognitiveclass.ai'
    ),
    (
        'https://chinjaaxiong-8000.theiadockernext-1-labs-'
        'prod-theiak8s-4-tor01.proxy.cognitiveclass.ai'
    ),
]

CSRF_TRUSTED_ORIGINS = [
    'http://127.0.0.1:8000/',
    (
        'https://chinjaaxiong-8000.theianext-1-labs-prod-'
        'misc-tools-us-east-0.proxy.cognitiveclass.ai'
    ),
    (
        'https://chinjaaxiong-8000.theiadockernext-1-labs-'
        'prod-theiak8s-4-tor01.proxy.cognitiveclass.ai'
    ),
]


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [],
}


INSTALLED_APPS = [
    'djangoapp.apps.DjangoappConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'djangoproj.urls'


TEMPLATES = [
    {
        'BACKEND': (
            'django.template.backends.django.DjangoTemplates'
        ),
        'DIRS': [
            os.path.join(BASE_DIR, 'frontend/static'),
            os.path.join(BASE_DIR, 'frontend/build'),
            os.path.join(BASE_DIR, 'frontend/build/static'),
        ],
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


WSGI_APPLICATION = 'djangoproj.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': (
            'django.contrib.auth.password_validation.'
            'UserAttributeSimilarityValidator'
        ),
    },
    {
        'NAME': (
            'django.contrib.auth.password_validation.'
            'MinimumLengthValidator'
        ),
    },
    {
        'NAME': (
            'django.contrib.auth.password_validation.'
            'CommonPasswordValidator'
        ),
    },
    {
        'NAME': (
            'django.contrib.auth.password_validation.'
            'NumericPasswordValidator'
        ),
    },
]


# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(STATIC_ROOT, 'media')
MEDIA_URL = '/media/'


# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


STATICFILES_DIRS = [
    os.path.join(
        BASE_DIR, 
        'frontend/static'
    ),
    os.path.join(
        BASE_DIR, 
        'frontend/build'
    ),
    os.path.join(
        BASE_DIR, 
        'frontend/build/static'
    ),
]
