from django.db import models

# Create your models here.


class CryptocurrencyExchange(models.Model):
    title = models.CharField()
    country = models.CharField()
    image = models.ImageField()
    trust_score = models.PositiveIntegerField()
    volume = models.PositiveIntegerField()
    cybersec_score = models.PositiveIntegerField()
