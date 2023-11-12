from django.contrib import admin

# Register your models here.

from.models import CryptocurrencyExchange

admin.site.register(CryptocurrencyExchange)
class CryptocurrencyExchangeAdmin(admin.ModelAdmin):
    list_display = '__all__'