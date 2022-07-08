# from django.contrib import admin
from django.urls import path
from . import views


# make updates here 

urlpatterns = [
    path('', views.home, name= "home"),
    path('reading.html', views.reading, name= "reading"),
    path('about.html', views.about, name= "about"),
    path('contact.html', views.contact, name= "contact"),
    path('confirmation.html', views.confirmation, name= "confirmation"),
    path('subscribe.html', views.subscribe, name= "subscribe"),
    path('math.html', views.math, name= "math"),
    path('addition.html', views.addition, name= "addition"),
    path('subtraction.html', views.subtraction, name= "subtraction"),
    path('multiplication.html',views.multiplication, name="multiplication"),



    

]