from django.db import models

from student.models import Student
from useful_variables import phone, LIST_OF_GRADES, TYPE_OF_ACTIVITY, SCHOOL_SUBJECT


class Teacher(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=40, default=None)
    phone_number = models.CharField(max_length=10, validators=[phone])
    address = models.TextField(max_length=100)

    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Grade(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='teacher')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='student')
    grade = models.CharField(max_length=12, choices=LIST_OF_GRADES)
    type_of_activity = models.CharField(max_length=12, choices=TYPE_OF_ACTIVITY)
    school_subject = models.CharField(max_length=20, choices=SCHOOL_SUBJECT)
    date = models.DateField()

    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
