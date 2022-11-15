from django import forms
from django.forms import TextInput, DateInput

from student.models import Student, GENDER_CHOICES, ENROLLMENT_CHOICES, STATUS


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student

        fields = ['first_name', 'last_name', 'status', 'date_of_birth', 'gender', 'CNP', 'enrollment']

        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'Please enter your first name', 'class': 'form-control'}),
            'last_name': TextInput(attrs={'placeholder': 'Please enter your last name', 'class': 'form-control'}),
            'status': forms.Select(choices=STATUS, attrs={'class': 'form-control'}),
            'date_of_birth': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'gender': forms.Select(choices=GENDER_CHOICES, attrs={'class': 'form-control'}),
            'CNP': TextInput(attrs={'placeholder': 'Please enter your CNP', 'class': 'form-control'}),
            'enrollment': forms.Select(choices=ENROLLMENT_CHOICES, attrs={'class': 'form-control'})
        }
