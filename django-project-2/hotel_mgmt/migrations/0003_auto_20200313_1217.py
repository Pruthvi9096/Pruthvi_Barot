# Generated by Django 2.1.15 on 2020-03-13 12:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_mgmt', '0002_auto_20200313_1144'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='checkIn_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='reservation',
            name='checkOut_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='reservation',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
