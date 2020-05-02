from django.db import models

class Tutorial(models.Model):

	title = models.CharField(max_length=100,blank=False,default='')
	description = models.TextField(max_length=200,blank=False,default='')
	published = models.BooleanField(default=False)

	def __str__(self):
		return self.title
