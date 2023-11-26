from django.db import models

# Create your models here.


class CryptocurrencyExchange(models.Model):

    name = models.CharField(max_length=100)
    short = models.CharField(max_length=3, default='aaa')
    country = models.CharField(max_length=100)
    image = models.ImageField()
    trust_score = models.PositiveIntegerField()
    volume = models.PositiveIntegerField()
    cybersec_score = models.PositiveIntegerField()

    def __str__(self) -> str:
        return f'{self.name}'


class Cryptocurrency(models.Model):

    name = models.CharField(max_length=100)
    short = models.CharField(max_length=3, default='sss')
    country = models.CharField(max_length=100)
    image = models.ImageField()
    course_current = models.PositiveIntegerField()
    course_1h = models.IntegerField()
    course_1d = models.IntegerField()
    course_1w = models.IntegerField()
    course_1m = models.IntegerField()
    volume = models.PositiveIntegerField()
    capitalization = models.PositiveIntegerField()

    def __str__(self) -> str:
        return f'{self.name}'
