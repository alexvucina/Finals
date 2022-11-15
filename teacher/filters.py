import django_filters
from django_filters import DateFilter

from teacher.models import Teacher


class TeacherFilter(django_filters.FilterSet):
    first_name = django_filters.CharFilter(lookup_expr='icontains', label='First name')
    last_name = django_filters.CharFilter(lookup_expr='icontains', label='Last name')
    phone_number = django_filters.CharFilter(lookup_expr='icontains', label='Phone number')
    address = django_filters.CharFilter(lookup_expr='icontains', label='Address')

    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 'phone_number', 'address']

    def __init__(self, *args, **kwargs):
        super(TeacherFilter, self).__init__(*args, **kwargs)

        self.filters['first_name'].field.widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter a first name'})
        self.filters['last_name'].field.widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter a last name'})
        self.filters['phone_number'].field.widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter the phone number'})
        self.filters['address'].field.widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter the address'})

