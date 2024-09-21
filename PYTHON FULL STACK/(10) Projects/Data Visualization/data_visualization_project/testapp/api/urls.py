from django.urls import include, path
from rest_framework import routers
from testapp.api.views import EnergyInsightAPI

router = routers.DefaultRouter()
router.register('energyinsight', EnergyInsightAPI)
urlpatterns = [
    path('', include(router.urls))
]
