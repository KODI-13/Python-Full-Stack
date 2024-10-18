from datetime import datetime
import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View
from testapp.models import EnergyInsight

# Create your views here.


class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()  # Convert datetime to ISO 8601 string format
        return super().default(obj)
    

def energy_data_json(request):
    data = list(EnergyInsight.objects.all().values())  # Get all data from the EnergyInsight model and  Convert QuerySet to a list of dictionaries
    context = {'data': json.dumps(data, cls=DateTimeEncoder)}
    return render(request, 'testapp/original.html', context)