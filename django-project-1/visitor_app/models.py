from django.db import models
from datetime import datetime
from django.http import *
from django.db.models import Q

class VisitFor(models.Model):
	name = models.CharField(max_length=50)
	department = models.ForeignKey('Department',on_delete=models.CASCADE)

	def __str__(self):
		return self.name

class Department(models.Model):
	department_name = models.CharField(max_length=25)

	def __str__(self):
		return self.department_name

class Visitor(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField(max_length=254)
	phone = models.CharField(max_length=20)
	address = models.TextField(max_length=250)
	image = models.ImageField(upload_to="image/")

	def __str__(self):
		return self.name

class VisitQuerySet(models.QuerySet):
	def search(self,query):
		lookup = (Q(visitor_name__name__icontains=query) |
				  Q(visitor_phone__iexact=query) |
				  Q(visitor_email__iexact=query) |	
				  Q(visit_to__name__icontains=query) |
				  Q(department__department_name__icontains=query) |
				  Q(purpose__icontains=query)
				)
		return self.filter(lookup)

class VisitManager(models.Manager):
	def get_queryset(self):
		return VisitQuerySet(self.model,using=self._db)

	def search(self,query=None):
		if query is None:
			return self.get_queryset().none()
		return self.get_queryset().search(query)

class Visit(models.Model):
	visitor_name = models.ForeignKey('Visitor',on_delete=models.CASCADE)
	visitor_phone = models.CharField(max_length=20)
	visitor_email = models.EmailField(max_length=250)
	visit_to = models.ForeignKey('VisitFor',on_delete=models.CASCADE)
	department = models.ForeignKey('Department',on_delete=models.CASCADE)
	purpose = models.CharField(max_length=150)
	checkOut_time = models.DateTimeField(null=True)
	checkIn_time = models.DateTimeField(null=True)

	objects = VisitManager()
	
def testcall():
    return HttpResponse("sucess")


