import pandas as pd
from django.core.management.base import BaseCommand
from BlogApp.models import Blog
from django.utils.dateparse import parse_datetime

class Command(BaseCommand):
    help = 'Import blogs from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file_path', type=str, help='The path to the CSV file to be imported')

    def handle(self, *args, **kwargs):
        csv_file_path = kwargs['csv_file_path']
        reader = pd.read_csv(csv_file_path)
        for _, row in reader.iterrows():
            blog = Blog(
                title=row['title'],
                content=row['content'],
                date_posted=parse_datetime(row['date_posted'])
            )
            blog.save()
        self.stdout.write(self.style.SUCCESS('Successfully imported blogs from CSV'))