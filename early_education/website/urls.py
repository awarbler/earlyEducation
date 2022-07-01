# from django.contrib import admin
from django.urls import path
from . import views


# make updates here 

urlpatterns = [
    path('', views.home, name= "home"),
    path('reading.html', views.reading, name= "reading"),
    path('science.html', views.science, name= "science"),
    path('math.html', views.math, name= "math"),
    path('addition.html', views.addition, name= "addition"),



    

]