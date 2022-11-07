from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('university/form/', views.university_form),
    path('university/list/', views.university_list),
    path('student/form/', views.student_form),
    path('student/list/', views.student_list)
    ]
