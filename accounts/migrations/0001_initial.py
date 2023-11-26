# Generated by Django 4.2.1 on 2023-11-26 22:35

import accounts.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('homepage', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(default='koteł.jpg', upload_to=accounts.models.user_avatar_image_path)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TransactionDiary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_profile', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='accounts.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('B', 'Buy'), ('S', 'Sell')], default='S', max_length=3)),
                ('volume', models.PositiveBigIntegerField()),
                ('date_of_transaction', models.DateField()),
                ('price_USD', models.PositiveBigIntegerField()),
                ('coin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.cryptocryptocurrency')),
                ('profile', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='accounts.userprofile')),
            ],
        ),
    ]
