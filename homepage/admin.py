from django.contrib import admin

# Register your models here.

from .models import CryptoCryptocurrencyExchange, CryptoCryptocurrency

admin.site.register(CryptoCryptocurrencyExchange)
admin.site.register(CryptoCryptocurrency)


class CryptocurrencyExchangeAdmin(admin.ModelAdmin):
    list_display = '__all__'


class CryptocurrencyAdmin(admin.ModelAdmin):
    list_display = '__all__'
