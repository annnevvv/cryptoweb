from rest_framework import serializers, permissions

from homepage.models import CryptocurrencyExchange

class CryptocurrencyExchangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CryptocurrencyExchange
        fields = '__all__'