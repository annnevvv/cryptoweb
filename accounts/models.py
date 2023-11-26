from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from homepage.models import Cryptocurrency
# Create your models here.


def user_avatar_image_path(instance, filename):
    return f'users/{instance.user.id}/avatar/{filename}'


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=user_avatar_image_path,
                               default='koteł.jpg')

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()


class TransactionDiary(models.Model):
    user_profile = models.OneToOneField(
        UserProfile, on_delete=models.CASCADE, default=None)
    # list_of_tr = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.user_profile.user.username} Diary'


@receiver(post_save, sender=UserProfile)
def create_user_tranasaction_diary(sender, instance, created, **kwargs):
    if created:
        TransactionDiary.objects.create(user_profile=instance)


@receiver(post_save, sender=UserProfile)
def save_user_tranasaction_diary(sender, instance, **kwargs):
    instance.transactiondiary.save()


class Transaction(models.Model):
    class Type(models.TextChoices):
        BUY = 'B'
        SELL = 'S'

    # TYPE_CHOICES = [(BUY, 'buy'), (SELL, 'sell')]

    diary = models.ForeignKey(
        TransactionDiary, on_delete=models.CASCADE)
    type = models.CharField(choices=Type.choices,
                            default=Type.SELL, max_length=3)
    volume = models.PositiveBigIntegerField()
    date_of_transaction = models.DateField()
    coin = models.ForeignKey(
        Cryptocurrency, on_delete=models.CASCADE)
    buy_price_USD = models.PositiveBigIntegerField()
    sell_price_USD = models.PositiveBigIntegerField()

    def __str__(self):
        return f'{self.coin} / {self.date_of_transaction} / {self.type}'
