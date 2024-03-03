from pathlib import Path
from dotenv import load_dotenv
import os
import logging

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ###############################################################################
# .ENV FILE & SECRET KEY
# ###############################################################################

env_path = BASE_DIR / '.env'
load_dotenv(dotenv_path=env_path)

print(f"DEBUG: .env path used: {env_path}")
print(f"DEBUG: DB_NAME from .env: {os.environ.get('DB_NAME')}")

SECRET_KEY = os.environ.get('SECRET_KEY', default='django-insecure-default-key')

# ###############################################################################
# ALLOWED HOSTS & CORS
# ###############################################################################

CORS_ALLOW_ALL_ORIGINS = True
ALLOWED_HOSTS = ['*']
cors_origins = os.environ.get('CORS_ALLOWED_ORIGINS', 'http://localhost:3000,http://localhost:3003,http://3.252.131.54:3001')
CORS_ALLOWED_ORIGINS = cors_origins.split(',')

print(f"ALLOWED_HOSTS: {ALLOWED_HOSTS}")
print(f"CORS_ALLOWED_ORIGINS: {CORS_ALLOWED_ORIGINS}")

# ###############################################################################
# DATABASES
# ###############################################################################

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST', 'localhost'),
        'PORT': os.environ.get('DB_PORT', ''),
    }
}

# ###############################################################################
# APPS & MIDDLEWARE
# ###############################################################################

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_filters',
    'rest_framework',
    'public_site',
    'corsheaders',
]

MIDDLEWARE = [
    'nano ~/.bashrc  # or replace with ~/.bash_profile, ~/.zshrc as per your shell.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

# ###############################################################################
# TEMPLATES
# ###############################################################################

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'public_site/templates/public'),
            os.path.join(BASE_DIR, 'public_site/templates/private'),
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

# ###############################################################################
# LOGGING & DEBUGGING
# ###############################################################################

DEBUG = os.environ.get("DEBUG", default=True) == 'True'  # Convert string to bool
print(f"DEBUG: {DEBUG}")

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'public_site/debug.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
        },
    },
}

# ###############################################################################
# INTERNATIONALIZATION
# ###############################################################################

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
