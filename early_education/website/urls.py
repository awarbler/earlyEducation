# from django.contrib import admin
from django.urls import path
from . import views


# make updates here 

urlpatterns = [
    path('', views.home, name= "home"),
    path('contact.html', views.contact, name= "contact"),
    path('about.html', views.about, name= "about"),
    path('math.html', views.math, name= "math"),
    path('why.html', views.why, name= "why"),



    

]