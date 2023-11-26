from rest_framework import viewsets

from django.shortcuts import render

from homepage.models import CryptoCryptocurrencyExchange, CryptoCryptocurrency
from .serializers import CryptocurrencyExchangeSerializer, CryptocurrencySerializer


class CryptocurrencyExchangeViewSet(viewsets.ModelViewSet):
    queryset = CryptoCryptocurrencyExchange.objects.all()
    serializer_class = CryptocurrencyExchangeSerializer


class CryptocurrencyViewSet(viewsets.ModelViewSet):
    queryset = CryptoCryptocurrency.objects.all()
    serializer_class = CryptocurrencySerializer
