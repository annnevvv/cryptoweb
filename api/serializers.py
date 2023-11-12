from rest_framework import serializers, permissions

from homepage.models import CryptocurrencyExchange, Cryptocurrency

class CryptocurrencyExchangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CryptocurrencyExchange
        fields = '__all__'

class CryptocurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Cryptocurrency
        fields = '__all__'