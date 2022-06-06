# from django.contrib import admin
from django.urls import path
from . import views


# make updates here 

urlpatterns = [
    path('', views.home, name="home"),

]