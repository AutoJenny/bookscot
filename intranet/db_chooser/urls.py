# db_chooser/urls.py
from django.urls import include, path
from . import api_views
from .api_views import fetch_data

app_name = 'db_chooser'

urlpatterns = [
    path('api/fetch-data/', api_views.fetch_data, name='fetch_data'),
    path('api/tables/', api_views.get_tables, name='get_tables'),
    path('api/columns/<str:table_name>/', api_views.get_columns, name='get_columns'),
]
