from django.shortcuts import render

def university_list(request):
    return render(request, "students_crud/university_list.html")

def university_form(request):
    return render(request, "students_crud/university_form.html")

def university_delete(request):
    return