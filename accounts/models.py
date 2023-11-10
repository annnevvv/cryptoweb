from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserAccountProfile(models.Model):
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.name


class TransactionDiary(models.Model):
    list_of_tr = models.CharField(0)