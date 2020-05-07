import csv

from django.core.management.base import BaseCommand, CommandError

from library.apps.authors.models import Author


class Command(BaseCommand):
    help = 'Import authors data to database'

    def add_arguments(self, parser):
        parser.add_argument('filename', help="Enter the .csv file")

    def handle(self, *args, **options):
        filename = options['filename']
        with open(filename) as f:
            f_csv = csv.DictReader(f)
            authors = []
            for row in f_csv:
                try:
                    author = Author(**row)
                except TypeError:
                    raise CommandError('Invalid file')
                else:
                    authors.append(author)
            Author.objects.bulk_create(authors)
        self.stdout.write(self.style.SUCCESS('Authors added successfully'))
