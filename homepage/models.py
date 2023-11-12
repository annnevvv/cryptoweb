from django.db import models

# Create your models here.


class CryptocurrencyExchange(models.Model):
    title = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    image = models.ImageField()
    trust_score = models.PositiveIntegerField()
    volume = models.PositiveIntegerField()
    cybersec_score = models.PositiveIntegerField()


class Cryptocurrency(models.Model):
    title = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    image = models.ImageField()
    course_current = models.PositiveIntegerField()
    course_1h = models.IntegerField()
    course_1d = models.IntegerField()
    course_1w = models.IntegerField()
    course_1m = models.IntegerField()
    volume = models.PositiveIntegerField()
    capitalization = models.PositiveIntegerField()
