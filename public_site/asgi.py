import os
from django.core.asgi import get_asgi_application

# Set the default Django settings module for the 'asgi' application.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'public_site.settings')

# Create an ASGI application instance for serving HTTP requests
application = get_asgi_application()
