from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView

from homepage.models import CryptoCryptocurrency, CryptoCryptocurrencyExchange

# Create your views here.


class HomepageView(View):
    template_name = 'accounts/index.html'

    def get(self, request, *args, **kwargs):
        crypto_cryptocurrency = CryptoCryptocurrency.objects.all()
        crypto_cryptocurrency_exchange = CryptoCryptocurrencyExchange.objects.all()

        context = {'crypto_cryptocurrency': crypto_cryptocurrency,
                   'crypto_cryptocurrency_exchange': crypto_cryptocurrency_exchange}

        return render(request, self.template_name, context)


class CryptocurrencyExchangeListView(ListView):
    template_name = 'index.html'


class CryptocurrencyExchangeDetailView(DetailView):
    template_name = 'index.html'
