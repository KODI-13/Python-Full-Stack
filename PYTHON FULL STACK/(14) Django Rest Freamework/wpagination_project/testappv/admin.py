from django.contrib import admin
from testappv.models import Employee

# Register your models here.
class EmplyeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'eno', 'ename', 'esal', 'eaddr']

admin.site.register(Employee, EmplyeeAdmin)