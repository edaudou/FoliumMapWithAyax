from unicodedata import name
from django.urls import path
from .import views

urlpatterns= [
    path('',views.index, name='index'),
    path('map/',views.map,name='map'),
    path('people/',views.people,name='people'),
]