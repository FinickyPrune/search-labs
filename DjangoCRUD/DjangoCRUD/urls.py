from django.contrib import admin
from django.urls import path, include

import students_crud

urlpatterns = [
    path('admin/', admin.site.urls),
    path('university/', include('students_crud.urls'))
]
