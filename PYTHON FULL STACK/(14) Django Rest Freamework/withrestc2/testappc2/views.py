from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from testappc2.serializers import NameSerializer

# Create your views here.
class TestAPIView(APIView):
    def get(self, request, *args, **kwargs):
        colors = ['red', 'green', 'blue', 'yellow']
        return Response({'msg':'My 1st Browsable API ', 'colors':colors})       # DRF provides special class called as Response() which is responsible for converting python dict to json data
    
    def post(self, request, *args, **kwargs):
        serializer = NameSerializer(data=request.data)          #*NOTE = it is diffferent from other serializer object we create earlier because we are directly passing the data coming from user to it and this serialization class is responsible for converting json data to python dict
        if serializer.is_valid():
            name = serializer.data.get('name')          #serializer.data is python data
            msg = 'hello {}, this is your 1st browsable API post request'.format(name)
            return Response({'msg':msg})
        else:
            return Response(serializer.errors, status=400)

    def put(self, request, *args, **kwargs):
        return Response({'msg':'This is from put method of APIView'})

    def patch(self, request, *args, **kwargs):
        return Response({'msg':'This is from patch method of APIView'})

    def delete(self, request, *args, **kwargs):
        return Response({'msg':'This is from delete method of APIView'})
    
# from rest_framework import viewsets         # from rest_framework package , viewsets module is imported
# class TestViewSet(viewsets.ViewSet): 

from rest_framework.viewsets import ViewSet     
class TestViewSet(ViewSet):
    def list(self, request, *args, **Kwargs):
        colors = ['red', 'green', 'blue', 'yellow']
        return Response({'msg':'Happy Sunday', 'colors':colors}) 
    
    def create(self, request, *args, **Kwargs):
        serializer = NameSerializer(data=request.data)          #*NOTE = it is diffferent from other serializer object we create earlier because we are directly passing the data coming from user to it and this serialization class is responsible for converting json data to python dict
        if serializer.is_valid():
            name = serializer.data.get('name')          #serializer.data is python data
            msg = 'hello {}, Destory Everything'.format(name)
            return Response({'msg':msg})
        else:
            return Response(serializer.errors, status=400)
        
    def retrieve(self, request, pk = None, *args, **Kwargs):
        return Response({'msg':'This is from retrive method of ViewSet'})
    
    def update(self, request, pk = None, *args, **Kwargs):
        return Response({'msg':'This is from update method of ViewSet'})

    def partial_update(self, request, pk = None, *args, **Kwargs):
        return Response({'msg':'This is from partial_update method of ViewSet'})

    def destroy(self, request, pk = None, *args, **Kwargs):
        return Response({'msg':'This is from destroy method of ViewSet'}) 


# go to 1_basic.txt Notes 
