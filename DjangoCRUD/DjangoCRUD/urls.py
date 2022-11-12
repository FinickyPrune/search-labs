from django.contrib import admin
from django.urls import path, include

from students_crud.models import Student, University

admin.site.register(Student)
admin.site.register(University)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('crud/', include('students_crud.urls')),
]
