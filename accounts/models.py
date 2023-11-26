from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.db.models import Sum, Avg

from homepage.models import CryptoCryptocurrency
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


class Transaction(models.Model):
    class Type(models.TextChoices):
        BUY = 'B'
        SELL = 'S'

    # TYPE_CHOICES = [(BUY, 'buy'), (SELL, 'sell')]

    # diary = models.ForeignKey(TransactionDiary, on_delete=models.CASCADE, default=None)
    profile = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, default=None)
    type = models.CharField(choices=Type.choices,
                            default=Type.SELL, max_length=3)
    volume = models.PositiveBigIntegerField()
    date_of_transaction = models.DateField()
    coin = models.ForeignKey(
        CryptoCryptocurrency, on_delete=models.CASCADE)
    price_USD = models.PositiveBigIntegerField()

    def summary_volume(self):
        vol = self.price_USD * self.volume
        if self.type == 'S':
            return vol
        else:
            return -vol

    def __str__(self):
        return f'{self.coin} / {self.date_of_transaction} / {self.type}'


class TransactionDiary(models.Model):

    user_profile = models.OneToOneField(
        UserProfile, on_delete=models.CASCADE, default=None)
    # list_of_tr = models.CharField(max_length=10)

    # transactions = Transaction.objects.filter(profile=user_profile)

    # def sum_usd(self, coin):
    #     total_volume = self.transactions.aggregate(Sum('summary_volume'))[
    #         'summary_volume__sum']
    #     return f'{total_volume}' or 0

    def sum_coin(self, coin):
        pass

    def avg_coin_sell(self, coin):
        pass

    def avg_coin_buy(self, coin):
        pass

    # def total_volume_for_coin(self, coin):
    #     total_volume = self.transactions.filter(
    #         coin=coin).aggregate(Sum('volume'))['volume__sum']
    #     return f'{total_volume}' or 0

    # def average_price_for_coin(self, coin):
    #     average_price = self.transactions.filter(
    #         coin=coin).aggregate(Avg('price_USD'))['price_USD__avg']
    #     return average_price or 0

    def __str__(self):
        return f'{self.user_profile.user.username} Diary'


@receiver(post_save, sender=UserProfile)
def create_user_tranasaction_diary(sender, instance, created, **kwargs):
    if created:
        TransactionDiary.objects.create(user_profile=instance)


@receiver(post_save, sender=UserProfile)
def save_user_tranasaction_diary(sender, instance, **kwargs):
    instance.transactiondiary.save()
