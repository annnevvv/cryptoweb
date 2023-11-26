from django.db import models

# Create your models here.


class CryptoCryptocurrencyExchange(models.Model):

    name = models.CharField(max_length=100)
    short = models.CharField(max_length=3, default='aaa')
    country = models.CharField(max_length=100)
    image = models.ImageField()
    trust_score = models.PositiveIntegerField()
    volume = models.PositiveIntegerField()
    liqudity = models.PositiveIntegerField(default=None)
    cybersec_score = models.PositiveIntegerField()

    def __str__(self) -> str:
        return f'{self.name}'


class CryptoCryptocurrency(models.Model):

    name = models.CharField(max_length=100)
    short = models.CharField(max_length=3, default='sss')
    country = models.CharField(max_length=100, default=None)
    image = models.ImageField(default=None)
    price_current = models.PositiveIntegerField(default=0)
    price_1h = models.IntegerField(default=0)
    price_1d = models.IntegerField(default=0)
    price_1w = models.IntegerField(default=0)
    price_1m = models.IntegerField(default=0)
    volume = models.PositiveIntegerField(default=0)
    capitalization = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return f'{self.name}'
