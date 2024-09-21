from django.shortcuts import render
from rest_framework.views import APIView
from testappc3.models import Employee
from testappc3.serializers import EmployeeSerializer
from rest_framework.response import Response


# Create your views here.

# class EmployeeListAPIView(APIView):
#     def get(self, request,format = None, *args, **kwargs):
#         qs = Employee.objects.all()         # model instance object
#         serialzer = EmployeeSerializer(qs, many=True)       # model instance object coverted into python dict
#         return Response(serialzer.data)          # DRF provides special class called as Response() which is responsible for converting python dict to json data

"""
for abaove there is an option to list out all records i.e. ListAPIView
"""
# from rest_framework.generics import ListAPIView

# class EmployeeListAPIView(ListAPIView):
#     queryset = Employee.objects.all()       # queryset is reserved keyword
#     serializer_class = EmployeeSerializer   # serializer_class is reserved keyword


# to perform search operation (in query string after ?ename=jay)
from rest_framework.generics import ListAPIView

class EmployeeListAPIView(ListAPIView):
    # queryset = Employee.objects.all()       # queryset is reserved keyword
    serializer_class = EmployeeSerializer   # serializer_class is reserved keyword
    def get_queryset(self):
        qs = Employee.objects.all()
        name = self.request.GET.get('ename')
        if name is not None:
            qs = qs.filter(ename__icontains=name)           # check iexact method
        return qs
    


# POST Operation using CrreateAPIView
from rest_framework.generics import CreateAPIView

class EmployeeCreateAPIView(CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    



# Retrieve Operation using CreateAPIView
from rest_framework.generics import RetrieveAPIView

class EmployeeRetrieveAPIView(RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    # lookup_field = 'id'     # ny specifything this we can use any name we want intead of pk in url configuration
    


# Update Operation using UpdateteAPIView
from rest_framework.generics import UpdateAPIView

class EmployeeUpdateAPIView(UpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    # lookup_field = 'id'     # ny specifything this we can use any name we want intead of pk in url configuration





# Delete Operation using DestroyAPIView
from rest_framework.generics import DestroyAPIView

class EmployeeDestroyAPIView(DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    # lookup_field = 'id'     # ny specifything this we can use any name we want intead of pk in url configuration



#=============================================================================================================================
"""
for performing two operations simultaneaously we have to use hybrid APIView classes as shown below
"""

# Listing and creating Operation using ListCreateAPIView
from rest_framework.generics import ListCreateAPIView

class EmployeeListCreateAPIView(ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    


# Retrieving and updating Operation using RetrieveUpdateAPIView
from rest_framework.generics import RetrieveUpdateAPIView

class EmployeeRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    # lookup_field = 'id'     # ny specifything this we can use any name we want intead of pk in url configuration


# Retrieving and Destroy Operation using RetrieveDestroyAPIView
from rest_framework.generics import RetrieveDestroyAPIView

class EmployeeRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    # lookup_field = 'id'     # ny specifything this we can use any name we want intead of pk in url configuration



# Retrieving, updating and Destroy Operation using RetrieveUpdateDestroyAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView

class EmployeeRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    # lookup_field = 'id'     # ny specifything this we can use any name we want intead of pk in url configuration



"""
Mixins concept
"""
# combination of modelMixin and APIView .......creating data using mixin and getting all data using ListAPIView
from rest_framework import mixins

class EmployeeListCreateModelMixin(mixins.CreateModelMixin, ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# Retrieving, updating and Destroy Operation using RetrieveUpdateDestroyAPIView
from rest_framework.generics import RetrieveAPIView
from rest_framework import mixins


class EmployeeRetrieveUpdateDestroyModelMixin(mixins.DestroyModelMixin, mixins.UpdateModelMixin, RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'id'     # ny specifything this we can use any name we want intead of pk in url configuration

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)