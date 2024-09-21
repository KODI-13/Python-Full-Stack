from hotel import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path(' /<id>',views.home),
    path('gallery/',views.gallery),
    path('about/',views.about),
    path('contact/',views.contact),
    path('booking/',views.booking, name='booking'), #(*NOTE = Reverse for 'booking' not found. 'booking' is not a valid view function or pattern name.  .... you have to give name in order to use it in form action like this <form action="{% url 'booking'%}">)
    path('king/',views.king),
    path('queen/',views.queen),
    path('suit/',views.suit),
    path('single/',views.single),
    path('double/',views.double),
    path('triple/',views.triple),
    
]