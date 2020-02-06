from django.db import models
from django.contrib.auth.models import User

class Hotel(models.Model):

	hotel_name  = models.CharField(max_length=100)
	address     = models.TextField(null=True,blank=True)
	contact     = models.CharField(max_length=80)
	email       = models.EmailField(max_length=60)
	hotel_image = models.ImageField(upload_to='image/')


class Facilities(models.Model):

	facility_name = models.CharField(max_length=100)


class Room(models.Model):

	room_number = models.IntegerField(null = False, blank = False, unique=True)
	capacity    = models.IntegerField()
	rate        = models.FloatField()
	facilities  = models.ManyToManyField('Facilities', related_name='room')
	hotel       = models.ForeignKey('Hotel', on_delete=models.SET_NULL, null=True)
	reserved    = models.BooleanField()

class Reservation(models.Model):

	customer = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
	room_id  = models.ManyToManyField('Room',related_name='reservation')
	total_price = models.FloatField()

