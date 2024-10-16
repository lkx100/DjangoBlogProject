import pandas as pd
from BlogApp.models import Blog
from django.utils.dateparse import parse_datetime

def import_blogs(csv_file_path):
    reader = pd.read_csv(csv_file_path)
    for _, row in reader.iterrows():
        blog = Blog(
            title=row['title'],
            content=row['content'],
            date_posted=parse_datetime(row['date_posted'])
        )
        blog.save()

if __name__ == "__main__":
    import_blogs("static/csv/blog_data.csv")