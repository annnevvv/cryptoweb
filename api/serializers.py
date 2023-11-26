from rest_framework import serializers, permissions

from homepage.models import CryptoCryptocurrencyExchange, CryptoCryptocurrency


class CryptocurrencyExchangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CryptoCryptocurrencyExchange
        fields = '__all__'


class CryptocurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = CryptoCryptocurrency
        fields = '__all__'
