from django.urls import path 
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('2',views.wonder,name="wonder"),
    path('3',views.chan,name="chan"),
    path('4',views.dora,name="dora"),
    path('5',views.krishna,name="krishna"),
    path('6',views.stuart,name="stuart"),
]
