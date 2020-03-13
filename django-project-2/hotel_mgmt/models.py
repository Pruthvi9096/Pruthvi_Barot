from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Hotel(models.Model):

	class Meta:
   		ordering = ['-id']

	hotel_name  = models.CharField(max_length=100)
	address     = models.TextField(null=True,blank=True)
	contact     = models.CharField(max_length=80)
	email       = models.EmailField(max_length=60)
	hotel_image = models.ImageField(upload_to='image/')

	def __str__(self):
		return self.hotel_name

class RoomFacilities(models.Model):

	class Meta:
   		ordering = ['-id']

	facility_name = models.CharField(max_length=50,null=False)

	def __str__(self):
		return self.facility_name

class RoomType(models.Model):

	class Meta:
   		ordering = ['-id']

	room_type = models.CharField(max_length=50,null=False)
	capacity = models.DecimalField(max_digits=2,decimal_places=1,null=True)
	facilities = models.ManyToManyField(RoomFacilities,related_name='roomtype')
	price = models.DecimalField(max_digits=6, decimal_places=2,null=True)
	room_image = models.ImageField(upload_to='image/')

	def __str__(self):
		return self.room_type

	def get_absolute_url(self):
		return reverse('room-type-detail',args=[str(self.id)])


class Room(models.Model):

	class Meta:
   		ordering = ['id']


	room_number = models.CharField(max_length=50,null=False,blank=False)
	room_type = models.ForeignKey(RoomType,null=True,on_delete=models.SET_NULL)
	reserved    = models.BooleanField()
	

	def __str__(self):
		return self.room_number

class Reservation(models.Model):

	def _get_hotel(self):
		return self.hotel.id

	class Meta:
   		ordering = ['-id']

	customer_name = models.CharField(max_length=150,null=False,blank=False)
	customer_address     = models.TextField(null=False,blank=True)
	customer_contact     = models.CharField(max_length=80,null=False)
	customer_email       = models.EmailField(max_length=60,null=False)
	room_type = models.ForeignKey(RoomType,null=True,on_delete=models.SET_NULL)
	room_id  = models.ManyToManyField('Room',related_name='reservation')
	days = models.DecimalField(max_digits=6, decimal_places=0,null=True)
	total_price = models.FloatField()
	checkOut_time = models.DateTimeField(null=True)
	checkIn_time = models.DateTimeField(null=True)
	created_on = models.DateTimeField(auto_now_add=True)

