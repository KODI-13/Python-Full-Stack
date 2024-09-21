from django.contrib import admin
from testapp.models import EnergyInsight

# Register your models here.
class EnergyInsightAdmin(admin.ModelAdmin):
        list_display = ['id', 'title', 'sector', 'topic', 'insight', 'url', 'region', 'start_year', 'end_year', 'impact', 'added', 'published', 'country', 'relevance', 'pestle', 'source', 'likelihood', 'intensity']

admin.site.register(EnergyInsight, EnergyInsightAdmin)