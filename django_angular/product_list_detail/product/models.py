from django.db import models

UNIT_CHOICES = [
('g','Gram'),
('kg','Kilogram'),
]

class Product(models.Model):

	name = models.CharField(max_length=150,null=False,blank=False)
	price = models.DecimalField(max_digits=6,decimal_places=2)
	stock = models.FloatField()
	unit = models.CharField(choices=UNIT_CHOICES,max_length=80)
	note = models.TextField(max_length=400)

	def __str__(self):
		return self.name

