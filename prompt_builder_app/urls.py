from rest_framework.routers import DefaultRouter
from django.urls import path, include 
from .views import ProcessTemplateView, DataSetViewSet, TemplateViewSet, ScriptViewSet, get_db_info, prompt_builder, test_template_view, available_databases, list_db_tables, list_table_columns, get_default_database # Add any additional views 
import logging

app_name = 'prompt_builder_app'
logger = logging.getLogger(__name__)

router = DefaultRouter()
router.register(r'datasets', DataSetViewSet)
router.register(r'templates', TemplateViewSet)
router.register(r'scripts', ScriptViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Default Router URLs
    path('test/', test_template_view, name='test_template'),
    path('prompt-builder/', prompt_builder, name='prompt_builder'),
    path('process/', ProcessTemplateView.as_view(), name='process_template'), 

    path('list-tables/', list_db_tables, name='list_tables'),
    
    path('databases/', include([ # Namespace for database-related endpoints
        path('', available_databases, name='available_databases'), # Keep existing available_databases 
    ])),  

    path('get-db-info/', get_db_info, name='get-db-info'),
    path('get-default-database/', get_default_database, name='get-default_database'),
    path('api/list-table-columns/<str:table_name>/', list_table_columns, name='list_table_columns'),
]