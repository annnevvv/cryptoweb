from django.shortcuts import render
from django.views import View

# Create your views here.

class DashboardView(View):
    template_name = 'dashboard.html'