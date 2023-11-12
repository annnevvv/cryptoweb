from django.contrib import admin

# Register your models here.

from.models import CryptocurrencyExchange, Cryptocurrency

admin.site.register(CryptocurrencyExchange)
admin.site.register(Cryptocurrency)
class CryptocurrencyExchangeAdmin(admin.ModelAdmin):
    list_display = '__all__'

class CryptocurrencyAdmin(admin.ModelAdmin):
    list_display = '__all__'