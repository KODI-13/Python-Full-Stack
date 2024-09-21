"""
URL configuration for withrestc3 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from testappc3 import views

urlpatterns = [
    path('admin/', admin.site.urls),


    path('api/', views.EmployeeListAPIView.as_view()),      #get all record
    path('api2/', views.EmployeeCreateAPIView.as_view()),   #post record
    path('api3/<pk>/', views.EmployeeRetrieveAPIView.as_view()),   #retrieve perticular record record
    path('api4/<pk>/', views.EmployeeUpdateAPIView.as_view()),   #update perticular record record
    path('api5/<pk>/', views.EmployeeDestroyAPIView.as_view()),   #Delete perticular record record

    path('api6/', views.EmployeeListCreateAPIView.as_view()),   #1st and 2nd url combination i.e list and create
    path('api7/<pk>/', views.EmployeeRetrieveUpdateAPIView.as_view()),   #3rd and 4th url combination i.e retrieve and update
    path('api8/<pk>/', views.EmployeeRetrieveDestroyAPIView.as_view()),   #3rd and 5th url combination i.e retrieve and Delete

    path('api9/<pk>/', views.EmployeeRetrieveUpdateDestroyAPIView.as_view()),   #3rd, 4th and 5th url combination i.e retrieve, update and Delete


    # these api is combination of modelMixin and APIView
    path('api10/', views.EmployeeListCreateModelMixin.as_view()),

    path('api11/<id>/', views.EmployeeRetrieveUpdateDestroyModelMixin.as_view())


]
