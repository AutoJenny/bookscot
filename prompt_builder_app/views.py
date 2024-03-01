from .forms import TestForm
from .models import DataSet, Template, Script
from .serializers import DataSetSerializer, TemplateSerializer, ScriptSerializer
from .template_processors.process import process_template
from django_filters.rest_framework import DjangoFilterBackend
from django.conf import settings
from django.db.utils import DatabaseError
from django.http import JsonResponse
from django.shortcuts import get_object_or_404 
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
import django_filters
from django.db import connection

import logging

logger = logging.getLogger(__name__)

def prompt_builder(request):
    print("prompt_builder view was called.")  # Temporary replacement
    print("This is a test debug log message")  
    try:
        # Attempt to render the prompt_builder template
        return render(request, 'prompt_builder/prompt_builder.html')
    except Exception as e:
        # Log any errors that occur during the rendering process
        logger.error(f"Error in prompt_builder view: {e}")
        # Optionally, you can re-raise the exception or handle it differently
        raise

def get_default_database(request):
    logger.debug("get_default_database called")
    default_database_name = settings.DATABASES['default']['NAME']  # Updated
    return JsonResponse({'defaultDatabase': default_database_name})  # Updated

# Define a filter class for DataSet
class DataSetFilter(django_filters.FilterSet):
    class Meta:
        model = DataSet
        fields = {
            'name': ['exact', 'icontains'],  # Example: Filter by name field
            # Add other fields you want to filter by
        }
        
# Define your viewsets

class ProcessTemplateView(APIView):
    def post(self, request, *args, **kwargs):
        # Your processing logic here
        # For example, extract template_id and data_set_id from request.data
        template_id = request.data.get('template_id')
        data_set_id = request.data.get('data_set_id')
        
        # Process the template and dataset...
        processed_text = "Some result based on the processing logic"
        
        # Return the result
        return Response({"processed_text": processed_text}, status=status.HTTP_200_OK)
    
class DataSetViewSet(viewsets.ModelViewSet):
    queryset = DataSet.objects.all()
    serializer_class = DataSetSerializer
    pagination_class = PageNumberPagination  # Enables pagination
    filter_backends = (DjangoFilterBackend, OrderingFilter,)
    filterset_class = DataSetFilter
    ordering_fields = ['name', 'created_at']  # Example: Fields that can be ordered
    ordering = ['created_at']  # Default ordering

class TemplateViewSet(viewsets.ModelViewSet):
    queryset = Template.objects.all()
    serializer_class = TemplateSerializer

    @action(detail=True, methods=['post'])
    def process_template(self, request, pk=None):
        template = self.get_object()
        data_set_id = request.data.get('data_set_id')
        if not data_set_id:
            return Response({"error": "data_set_id not provided"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            processed_text = process_template(template.id, data_set_id)
            return Response({"processed_text": processed_text})
        except DataSet.DoesNotExist:
            return Response({"error": "DataSet not found"}, status=status.HTTP_404_NOT_FOUND)

class ScriptViewSet(viewsets.ModelViewSet):
    queryset = Script.objects.all()
    serializer_class = ScriptSerializer


# Define any standalone views or utility functions
def test_template_view(request):
    processed_text = ""
    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            template = form.cleaned_data['template']
            data_set = form.cleaned_data['data_set']
            processed_text = process_template(template.id, data_set.id)
    else:
        form = TestForm()
    return render(request, 'prompt_builder_app/test_template.html', {
        'form': form, 
        'processed_text': processed_text
    })

def available_databases():  # Remove 'request'
    databases = settings.DATABASES.keys()
    return JsonResponse({'databases': list(databases)})

def get_db_info():  # Remove 'request'
    logger.debug("get_db_info called")
    default_database_name = settings.DATABASES['default']['NAME']
    return JsonResponse({'defaultDatabase': default_database_name})

def list_db_tables(request):
    with connection.cursor() as cursor:
        cursor.execute("SHOW TABLES")
        tables = [row[0] for row in cursor.fetchall()]
    return JsonResponse({'tables': tables})

def list_table_columns(request, table_name):
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"SHOW COLUMNS FROM {table_name}")
            columns = [row[0] for row in cursor.fetchall()]
        return JsonResponse({'columns': columns})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


