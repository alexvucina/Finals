from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from student.filters import StudentFilter
from student.forms import StudentForm
from student.models import Student


class StudentCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = 'student/create_student.html'
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy('homepage')
    permission_required = 'student.add_student'

    def get_context_data(self, **kwargs):
        data = super(StudentCreateView, self).get_context_data(**kwargs)
        students = Student.objects.all()
        data['all_students'] = students

        return data


class StudentsListView(LoginRequiredMixin, PermissionRequiredMixin,ListView):
    template_name = 'student/list_of_students.html'
    model = Student
    context_object_name = 'all_students'
    permission_required = 'student.view_list_of_students'

    def get_context_data(self, **kwargs):
        data = super(StudentsListView, self).get_context_data(**kwargs)
        students = Student.objects.all()
        my_filter = StudentFilter(self.request.GET, queryset=students)
        students = my_filter.qs
        data['all_students'] = students
        data['my_filter'] = my_filter.form

        return data


class StudentUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'student/update_student.html'
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy('list_of_students')
    permission_required = 'student.update_student'


class StudentDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    template_name = 'student/delete_student.html'
    model = Student
    success_url = reverse_lazy('list_of_students')
    permission_required = 'student.delete_student'


class StudentDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    template_name = 'student/details_student.html'
    model = Student
    permission_required = 'student.view_student_details'
