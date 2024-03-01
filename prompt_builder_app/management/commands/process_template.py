from django.core.management.base import BaseCommand
from prompt_builder_app.models import Template, DataSet
from prompt_builder_app.template_processors.process import process_template

class Command(BaseCommand):
    help = 'Processes a template with a specified dataset'

    def add_arguments(self, parser):
        parser.add_argument('template_id', type=int, help='ID of the template')
        parser.add_argument('data_set_id', type=int, help='ID of the dataset')

    def handle(self, *args, **options):
        template_id = options['template_id']
        data_set_id = options['data_set_id']
        try:
            result = process_template(template_id, data_set_id)
            self.stdout.write(self.style.SUCCESS(f'Processed Text: \n{result}'))
        except Template.DoesNotExist:
            self.stdout.write(self.style.ERROR('Template not found'))
        except DataSet.DoesNotExist:
            self.stdout.write(self.style.ERROR('DataSet not found'))
