import django_filters
from django import forms
from django.db import models

from django_filters import DateFilter

from parent.models import Parent


class ParentFilter(django_filters.FilterSet):
    first_name = django_filters.CharFilter(lookup_expr='icontains', label='First name')
    last_name = django_filters.CharFilter(lookup_expr='icontains', label='Last name')

    class Meta:
        model = Parent
        fields = ['first_name', 'last_name', 'parent_type', 'student', 'phone_number', 'email' ]

    def __init__(self, *args, **kwargs):
        super(ParentFilter, self).__init__(*args, **kwargs)

        self.filters['first_name'].field.widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter a first name'})
        self.filters['last_name'].field.widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter a last name'})
        # self.filters['status'].field.widget.attrs.update({'class': 'form-select'})
        # self.filters['gender'].field.widget.attrs.update({'class': 'form-select'})
        # self.filters['enrollment'].field.widget.attrs.update({'class': 'form-select'})
