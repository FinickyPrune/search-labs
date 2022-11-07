from django.contrib import admin
from django.urls import path, include

import students_crud

urlpatterns = [
    path('admin/', admin.site.urls),
    path('crud/', include('students_crud.urls')),
]
