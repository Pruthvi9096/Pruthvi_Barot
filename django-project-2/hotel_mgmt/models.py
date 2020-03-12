from django.db import models
from django.contrib.auth.models import User

class Hotel(models.Model):

	hotel_name  = models.CharField(max_length=100)
	address     = models.TextField(null=True,blank=True)
	contact     = models.CharField(max_length=80)
	email       = models.EmailField(max_length=60)
	hotel_image = models.ImageField(upload_to='image/')

	def __str__(self):
		return self.hotel_name

class RoomFacilities(models.Model):
	facility_name = models.CharField(max_length=50,null=False)

	def __str__(self):
		return self.facility_name

class Room(models.Model):

	room_choices = [
		('r','Regular'),
		('p','Professional'),
		('e','Exclusive')
	]

	room_number = models.CharField(max_length=50,null=False,blank=False)
	capacity = models.DecimalField(max_digits=2,decimal_places=1,null=True)
	room_type = models.CharField(choices=room_choices,default='r',max_length=25)
	facilities = models.ManyToManyField(RoomFacilities,related_name='room')
	reserved    = models.BooleanField()
	hotel       = models.ForeignKey('Hotel', on_delete=models.SET_NULL, null=True)

	def __str__(self):
		return self.room_number

class Reservation(models.Model):

	customer = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
	room_id  = models.ManyToManyField('Room',related_name='reservation')
	total_price = models.FloatField()
	hotel      = models.ForeignKey('Hotel', on_delete=models.CASCADE, null=False,blank=False)

