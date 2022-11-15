from django.db import models

from useful_variables import STATUS, GENDER_CHOICES, cnp, ENROLLMENT_CHOICES


class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    status = models.CharField(max_length=8, choices=STATUS, null=False, default='Active')
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    CNP = models.CharField(max_length=13, validators=[cnp])
    enrollment = models.CharField(max_length=17, choices=ENROLLMENT_CHOICES)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
