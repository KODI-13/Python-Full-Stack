from django.db import models

# Create your models here.
class EnergyInsight(models.Model):
    title = models.CharField(max_length=255)
    sector = models.CharField(max_length=100)
    topic = models.CharField(max_length=100)
    insight = models.CharField(max_length=255)
    url = models.URLField(max_length=255)
    region = models.CharField(max_length=100)
    start_year = models.CharField(max_length=4, blank=True, null=True)
    end_year = models.CharField(max_length=4, blank=True, null=True)
    impact = models.TextField(blank=True, null=True)
    added = models.DateTimeField(blank=True, null=True)
    published = models.DateTimeField(blank=True, null=True)
    country = models.CharField(max_length=100)
    relevance = models.IntegerField()
    pestle = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    likelihood = models.IntegerField()
    intensity = models.IntegerField()

    def __str__(self):
        return f"{self.title} - {self.country}"