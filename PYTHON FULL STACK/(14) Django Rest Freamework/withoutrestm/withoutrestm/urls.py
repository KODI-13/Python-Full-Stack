"""
URL configuration for withoutrestm project.

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
from testappm import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # # 2 endpoints to perform crud operation 
    # path('api/<id>/', views.EmplyeeDetailCBV.as_view()),
    # path('api/', views.EmployeeListCBV.as_view()),

    # Single endpoint to perform crud operation
    path('api/', views.EmployeeCRUDCBV.as_view())

]
