from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserAccountProfile(models.Model):
    users = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class TransactionDiary(models.Model):
    list_of_tr = models.CharField(max_length=100)