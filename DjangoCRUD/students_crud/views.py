from django.shortcuts import render, redirect
from .forms import UniversityForm, StudentForm
from .models import University, Student


def university_list(request):
    context = {'university_list': University.objects.all()}
    return render(request, "students_crud/university_list.html", context)


def university_form(request):
    if request.method == "GET":
        form = UniversityForm()
        return render(request, "students_crud/university_form.html", {'form': form})
    else:
        form = UniversityForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/crud/university/list')


def university_delete(request):
    return


def student_list(request):
    context = {'student_list': Student.objects.all()}
    return render(request, "students_crud/students_list.html", context)


def student_form(request):
    if request.method == "GET":
        form = StudentForm()
        return render(request, "students_crud/students_form.html", {'form': form})
    else:
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/crud/student/list')


def student_delete(request):
    return
