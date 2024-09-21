from django.shortcuts import render
from testappv.models import Employee
from testappv.serializers import EmployeeSerializer
from rest_framework import generics
from testappv.pagination import MyPagination, MyPagination2, MyPagination3

# Create your views here.
class EmployeeListView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    # pagination_class = MyPagination3   # if it is commennted hten global pagination will apply on dataset
    # *NOTE = but to define the page size it is highly recommended to take separte class with custom properties

    # def get_queryset(self):
    #     qs = Employee.objects.all()
    #     name = self.request.GET.get('ename')    # taking data provided by partner application for query parameter in url
    #     if name is not None:
    #         qs = qs.filter(ename__icontains=name) # this line means in queryset if ename(employee name) coontains provided name then filtered(return) that record
    #     return qs

    # # In settings.py default filtering is added in REST_FRAMEWORK instead of above commented get_queryset method
    # search_fields = ('ename','eno')    # search based on ename and eno
    # search_fields = ('^eno',)    # search based on eno starts with perticular number
    search_fields = ('=eno',)    # search based on eno with exactly provided eno
    ordering_fields= ('eno','esal') # ordering based on eno and esal if these fields are not specified then default value is '__all__'





    