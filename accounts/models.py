from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class UserAccountProfile(models.Model):
    users = models.ForeignKey(User, on_delete=models.CASCADE)
    avatar = models.ImageField()

    def __str__(self):
        return self.name


class TransactionDiary(models.Model):
    list_of_tr = models.CharField(max_length=100)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserAccountProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofilemodel.save()
