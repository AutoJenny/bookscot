import logging
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.db import connection

# Configure logging for this module
logger = logging.getLogger(__name__)

@require_http_methods(["GET"])
def fetch_data(request):
    logger.info("fetch_data view has been called")
    
    table = request.GET.get('table')
    columns = request.GET.getlist('column')
    row_id = request.GET.get('row_id')

    if not (table and columns and row_id):
        logger.warning("Missing required parameters in fetch_data request")
        return JsonResponse({'error': 'Missing required parameters.'}, status=400)

    columns_joined = ", ".join(columns)
    query = f"SELECT {columns_joined} FROM {table} WHERE id = %s"

    try:
        with connection.cursor() as cursor:
            cursor.execute(query, [row_id])
            row = cursor.fetchone()
    except Exception as e:
        logger.error(f"Database error in fetch_data: {e}", exc_info=True)
        return JsonResponse({'error': 'Database error.'}, status=500)

    if row:
        data = dict(zip(columns, row))
        logger.debug(f"Data fetched successfully in fetch_data: {data}")
        return JsonResponse({'data': data})
    else:
        logger.info("No data found in fetch_data.")
        return JsonResponse({'error': 'No data found.'}, status=404)

#def get_tables(request):
#    db_name = 'aibos_django'
#    query = "SELECT table_name FROM information_schema.tables WHERE table_schema = %s"
#    
#    logger.info("get_tables view has been called")
#    
#    try:
#        with connection.cursor() as cursor:
#            cursor.execute(query, [db_name])
#            tables = [row[0] for row in cursor.fetchall()]
#    except Exception as e:
#        logger.error(f"Database error in get_tables: {e}", exc_info=True)
#        return JsonResponse({'error': 'Database error.'}, status=500)

#    logger.debug(f"Tables fetched successfully in get_tables: {tables}")
#    return JsonResponse({'tables': tables})

def get_tables(request):
    logger.info("get_tables view has been called")
    return JsonResponse({'tables': ['table1', 'table2']})

def get_columns(request, table_name):
    logger.info("get_columns view has been called")
    
    # Placeholder for actual implementation
    logger.warning("get_columns function is not yet implemented")
    
    return JsonResponse({'error': 'Function not implemented.'}, status=501)
