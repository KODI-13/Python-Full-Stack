from rest_framework.viewsets import ModelViewSet
from testapp.api.serializers import EnergyInsightSerializer
from testapp.models import EnergyInsight 

class EnergyInsightAPI(ModelViewSet):
    queryset = EnergyInsight.objects.all()
    serializer_class = EnergyInsightSerializer