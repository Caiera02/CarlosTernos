"""
Django settings for app project.

Generated by 'django-admin startproject' using Django 5.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-8er3!#0$6%qqfk)866(*3kk5egy+e7c0i0t1@sfqwd1jaux==3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'produtos',
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

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['app/templates'],
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

WSGI_APPLICATION = 'app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'carlos',
#         'USER': 'postgres',
#         'PASSWORD': 'heveca123567',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = [  os.path.join(BASE_DIR, 'static')    ]

STATIC_ROOT = BASE_DIR / "staticfiles"


# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

JAZZMIN_SETTINGS = {

    # title of the window (Will default to current_admin_site.site_title if absent or None)
    'site_title': 'Carlos Ternos',

    # Title on the login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    'site_header': 'Carlos Ternos',

    # Title on the brand (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    'site_brand': 'Carlos Ternos',
    
    # Logo to use for your site, must be present in static files, used for brand on top left
    "site_logo": "IMG/logo_P.svg",
    
    # Logo to use for your site, must be present in static files, used for login form logo (defaults to site_logo)
    "login_logo": "IMG/logo.svg",

    # Logo to use for login form in dark themes (defaults to login_logo)
    # "login_logo_dark": "IMG/Capa.png",
    
    'icons': {
        'auth': 'fas fa-users-cog',
        'auth': 'fas fa-star',
        'auth.user': 'fas fa-user',
        'auth.Group': 'fas fa-users',
    },

    # Welcome text on the login screen
    'welcome_sign': 'Bem-vindo(a) ao System Caio',
   
    # Copyright on the footer
    'copyright': 'Carlos Ternos LTDA',

    # Links to put along the top menu
    "topmenu_links": [

        # Url that gets reversed (Permissions can be added)
        {"name": "Home",  "url": "admin:index", "permissions": ["auth.view_user"]},

        # external url that opens in a new window (Permissions can be added)
        {"name": "Visualizar", "url": "http://127.0.0.1:8000/img/?search=and", "new_window": True},
        {"name": "Abrir chamado", "url": "http://127.0.0.1:8000/admin/tickets/ticket/add/", "new_window":True},

        # model admin to link to (Permissions checked against model)
        # {"model": "auth.User"},

        # App with dropdown menu to all its models pages (Permissions checked against models)
        {"app": "books"},
    ],
    # List of model admins to search from the search bar, search bar omitted if excluded
    # If you want to use a single search field you dont need to use a list, you can use a simple string
    #'search_model': ['products.Controle'], # Faz uma busca no model, fica no top do site

    # Whether to show the UI customizer on the sidebar
    'show_ui_builder': False, # Alteração das cores,layout etc
}

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


