# Generated by Django 2.1.15 on 2020-03-11 03:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Facilities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facility_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_name', models.CharField(max_length=100)),
                ('address', models.TextField(blank=True, null=True)),
                ('contact', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=60)),
                ('hotel_image', models.ImageField(upload_to='image/')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.FloatField()),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.IntegerField(unique=True)),
                ('capacity', models.IntegerField()),
                ('rate', models.FloatField()),
                ('reserved', models.BooleanField()),
                ('facilities', models.ManyToManyField(related_name='room', to='hotel_mgmt.Facilities')),
                ('hotel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hotel_mgmt.Hotel')),
            ],
        ),
        migrations.AddField(
            model_name='reservation',
            name='room_id',
            field=models.ManyToManyField(related_name='reservation', to='hotel_mgmt.Room'),
        ),
    ]
