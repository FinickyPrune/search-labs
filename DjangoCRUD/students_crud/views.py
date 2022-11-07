from django.shortcuts import render
from .forms import UniversityForm, StudentForm


def university_list(request):
    return render(request, "students_crud/university_list.html")


def university_form(request):
    form = UniversityForm()
    return render(request, "students_crud/university_form.html", {'form': form})


def university_delete(request):
    return


def student_list(request):
    return render(request, "students_crud/students_list.html")


def student_form(request):
    form = StudentForm()
    return render(request, "students_crud/students_form.html", {'form': form})


def student_delete(request):
    return


