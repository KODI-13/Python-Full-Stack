from rest_framework import serializers
from testapp.models import EnergyInsight

class EnergyInsightSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnergyInsight
        fields = '__all__'