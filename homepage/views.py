from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView

# Create your views here.


class HomepageView(View):
    template_name = 'index.html'

class CryptocurrencyExchangeListView(ListView):
    template_name = 'index.html'
class CryptocurrencyExchangeDetailView(DetailView):
    template_name = 'index.html'