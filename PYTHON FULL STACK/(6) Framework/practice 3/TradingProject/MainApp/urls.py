from MainApp import views
from django.urls import include, path

urlpatterns = [
    path('', views.home),

]