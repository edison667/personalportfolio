from django.urls import path

from .views import *
#from django import views

urlpatterns = [
    path('', allblogs, name='allblogs'),
    path('<int:blog_id>', detail, name='detail'),


]
