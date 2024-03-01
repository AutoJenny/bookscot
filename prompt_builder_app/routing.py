# prompt_builder_app/routing.py

from django.urls import re_path
from .consumers import MyConsumer

websocket_urlpatterns = [
    re_path(r'^ws/live-updates/$', MyConsumer.as_asgi()),
]
