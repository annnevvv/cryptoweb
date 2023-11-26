from django.db import models

# Create your models here.


class CryptocurrencyExchange(models.Model):

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


class Cryptocurrency(models.Model):

    name = models.CharField(max_length=100)
    short = models.CharField(max_length=3, default='sss')
    country = models.CharField(max_length=100)
    image = models.ImageField()
    price_current = models.PositiveIntegerField()
    price_1h = models.IntegerField()
    price_1d = models.IntegerField()
    price_1w = models.IntegerField()
    price_1m = models.IntegerField()
    volume = models.PositiveIntegerField()
    capitalization = models.PositiveIntegerField()

    def __str__(self) -> str:
        return f'{self.name}'
