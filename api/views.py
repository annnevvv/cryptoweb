from rest_framework import viewsets

from django.shortcuts import render

from homepage.models import CryptocurrencyExchange
from serializers import CryptocurrencyExchangeSerializer
# Create your views here.

class CryptocurrencyExchangeViewSet(viewsets.ModelViewSet):
    queryset = CryptocurrencyExchange.objects.all()
    serializer_class = CryptocurrencyExchangeSerializer