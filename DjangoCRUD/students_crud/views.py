from django.shortcuts import render, redirect
from .forms import UniversityForm, StudentForm
from .models import University, Student


def university_list(request):
    context = {'university_list': University.objects.all()}
    return render(request, "students_crud/university_list.html", context)


def university_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = UniversityForm()
        else:
            university = University.objects.get(pk=id)
            form = UniversityForm(instance=university)
        return render(request, "students_crud/university_form.html", {'form': form})
    else:
        if id == 0:
            form = UniversityForm(request.POST)
        else:
            university = University.objects.get(pk=id)
            form = UniversityForm(request.POST, instance=university)
        if form.is_valid():
            form.save()
        return redirect('/crud/university/list')


def university_delete(request):
    return


def student_list(request):
    context = {'student_list': Student.objects.all()}
    return render(request, "students_crud/students_list.html", context)


def student_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = StudentForm()
        else:
            student = Student.objects.get(pk=id)
            form = StudentForm(instance=student)
        return render(request, "students_crud/students_form.html", {'form': form})
    else:
        if id == 0:
            form = StudentForm(request.POST)
        else:
            student = Student.objects.get(pk=id)
            form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
        return redirect('/crud/student/list')


def student_delete(request):
    return
