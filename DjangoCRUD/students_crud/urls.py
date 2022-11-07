from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.university_form), #localhost/university/
    path('list/', views.university_list)
]