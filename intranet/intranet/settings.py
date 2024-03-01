import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
env_path = Path(__file__).resolve().parent.parent.parent / '.env'
load_dotenv(dotenv_path=env_path)
print(f"DEBUG: .env path used: {env_path}")
print(f"DEBUG: DB_NAME from .env: {os.environ.get('DB_NAME')}")


ROOT_URLCONF = 'intranet.urls'

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_filters',
    'rest_framework',
    'channels',
    'corsheaders',
    'django_extensions',
    'db_chooser',  # Your custom app
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # CORS middleware
]

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

WSGI_APPLICATION = 'intranet.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST', 'localhost'), 
        'PORT': os.environ.get('DB_PORT'),
    }
}

# Password validation, Internationalization, Static files settings are fine

print(f"DB_NAME: {os.environ.get('DB_NAME')}")
print(f"DB_USER: {os.environ.get('DB_USER')}")
print(f"DB_PASSWORD: {os.environ.get('DB_PASSWORD')}")
print(f"DB_HOST: {os.environ.get('DB_HOST')}")
print(f"DB_PORT: {os.environ.get('DB_PORT')}")

# CORS configuration
CORS_ALLOW_ALL_ORIGINS = True  # Allow all origins for simplicity
CORS_ALLOWED_ORIGINS = os.environ.get('CORS_ALLOWED_ORIGINS', default=['http://localhost:3000', 'http://3.252.131.54:3001'])

# ASGI application settings for channels
ASGI_APPLICATION = 'intranet.asgi.application'

# Static files settings are fine

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Logging settings
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': '/var/www/aibos/intranet/intranet/debug.log',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',  # Captures all Django-related logs
            'propagate': True,
        },
        'db_chooser': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',  # Adjust as needed for your app-specific logs
            'propagate': False,
        },
    },
}

# Print the environment being used, for verification
print(f"DEBUG: {DEBUG}")
print(f"ALLOWED_HOSTS: {ALLOWED_HOSTS}")
print(f"CORS_ALLOWED_ORIGINS: {CORS_ALLOWED_ORIGINS}")
