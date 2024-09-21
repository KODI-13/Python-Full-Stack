from django.shortcuts import render
from django.views.generic import View
# Create your views here.
class EnergyInsightViewCBV(View):
    def get(self, request):
        return render(request, 'testapp\dashboard.html')