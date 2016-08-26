import csv
from django.core.management.base import BaseCommand
from starwars.models import Characters


class Command(BaseCommand):
    help = 'Export all characters to CSV'

    def add_arguments(self, parser):
        parser.add_argument('output', type=str, help="Destination path for CSV file")

    def handle(self, *args, **options):
        characters = Characters.objects.order_by('name')

        writer = csv.writer(open(options['output'], 'w'))

        headers = []
        for field in Characters._meta.fields:
            headers.append(field.name)
        writer.writerow(headers)

        for char in characters:
            row = []
            for field in headers:
                val = getattr(char, field)
                row.append(val)
            writer.writerow(row)
        self.stdout.write(self.style.SUCCESS('Successfully exported to %s' % options['output']))