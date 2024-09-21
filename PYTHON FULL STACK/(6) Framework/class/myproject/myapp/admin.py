from django.contrib import admin

# Register your models here.
from myapp.models import Details,Employee
admin.site.register(Details)
admin.site.register(Employee)