from django.db import models


class University(models.Model):
    full_name = models.CharField(max_length=50)
    shorten_name = models.CharField(max_length=50)
    foundation_date = models.DateField()


class Student(models.Model):
    full_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    enter_year = models.IntegerField()
    university = models.ForeignKey(University, on_delete=models.SET_NULL, null=True)
