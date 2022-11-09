from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('university/form/', views.university_form, name='university_create'),
    path('university/form/<int:id>/', views.university_form, name='university_update'),
    path('university/list/', views.university_list, name='university_read'),
    path('student/form/', views.student_form, name='student_create'),
    path('student/form/<int:id>/', views.student_form, name='student_update'),
    path('student/list/', views.student_list, name='student_read')
    ]
