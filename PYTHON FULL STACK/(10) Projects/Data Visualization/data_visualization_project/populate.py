import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE','data_visualization_project.settings')
django.setup()

from datetime import datetime
from django.utils import timezone
import json
from testapp.models import *

# Helper function to convert empty strings to default values for numerical fields
def safe_int(value, default=0):
    if value == '':
        return default
    try:
        return int(value)
    except (ValueError, TypeError):
        return default


with open("C:/Deepak/PYTHON FULL STACK/(10) Projects/Data Visualization/data_visualization_project/jsondata.json","r", encoding='utf-8') as f:
    data = json.load(f)
    for item in data:
        # Handle possible empty or missing date fields
        added_date = item.get('added')
        added = timezone.make_aware(datetime.strptime(added_date, '%B, %d %Y %H:%M:%S')) if added_date else None

        published_date = item.get('published')
        published = timezone.make_aware(datetime.strptime(published_date, '%B, %d %Y %H:%M:%S')) if published_date else None

            
        EnergyInsight.objects.create(
                    title=item.get('title'),
                    sector=item.get('sector'),
                    topic=item.get('topic'),
                    insight=item.get('insight'),
                    url=item.get('url'),
                    region=item.get('region'),
                    start_year=item.get('start_year', None),
                    end_year=item.get('end_year', None),
                    impact=item.get('impact', None),
                    added=added,
                    published=published,
                    country=item.get('country'),
                    relevance=safe_int(item.get('relevance')),  # Convert to integer, default 0 if empty
                    pestle=item.get('pestle', None),
                    source=item.get('source', None),
                    likelihood=safe_int(item.get('likelihood')),  # Convert to integer, default 0 if empty
                    intensity=safe_int(item.get('intensity'))  # Convert to integer, default 0 if empty
                )

        
    print(data)  