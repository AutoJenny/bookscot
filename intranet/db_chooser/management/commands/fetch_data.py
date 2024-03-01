# api_views.py
from django.core.management.base import BaseCommand
from django.db import connection
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET"])
def fetch_data_api(request):
    # Extract parameters from request
    table = request.GET.get('table')
    columns = request.GET.getlist('column')  # Handles multiple column parameters
    row_id = request.GET.get('row_id')

    # Construct and execute the SQL query
    columns_joined = ", ".join(columns)
    query = f"SELECT {columns_joined} FROM {table} WHERE id = %s"
    with connection.cursor() as cursor:
        cursor.execute(query, [row_id])
        row = cursor.fetchone()

    # Format and return the response
    if row:
        data = dict(zip(columns, row))
        return JsonResponse({'data': data})
    else:
        return JsonResponse({'error': 'No data found.'}, status=404)

class Command(BaseCommand):
    help = 'Fetches data from a specified table, columns, and row.'

    def add_arguments(self, parser):
        parser.add_argument('--table', type=str, help='Table name')
        parser.add_argument('--columns', nargs='+', help='Column names (space-separated)')
        parser.add_argument('--row_id', type=int, help='ID of the row to fetch')

    def handle(self, *args, **options):
        table = options['table']
        columns = ", ".join(options['columns'])
        row_id = options['row_id']

        with connection.cursor() as cursor:
            cursor.execute(f"SELECT {columns} FROM {table} WHERE id = %s", [row_id])
            row = cursor.fetchone()
            if row:
                self.stdout.write(self.style.SUCCESS(f'Row data: {row}'))
            else:
                self.stdout.write(self.style.ERROR('No data found.'))
