from rest_framework import viewsets

from django.shortcuts import render

from homepage.models import CryptocurrencyExchange, Cryptocurrency
from .serializers import CryptocurrencyExchangeSerializer, CryptocurrencySerializer


class CryptocurrencyExchangeViewSet(viewsets.ModelViewSet):
    queryset = CryptocurrencyExchange.objects.all()
    serializer_class = CryptocurrencyExchangeSerializer

class CryptocurrencyViewSet(viewsets.ModelViewSet):
    queryset = Cryptocurrency.objects.all()
    serializer_class = CryptocurrencySerializer