from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView


class HomeTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'home/homepage.html'
