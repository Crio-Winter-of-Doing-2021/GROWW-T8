from django.db import models
from accounts.models import Profile

CATEGORIES = [
	('ST', 'Stocks'),
	('MF', 'Mutual Funds'),
	('GO', 'Gold'),
	('FD', 'Fixed Deposits')
]

STATUS = [
	('PR', 'Processing'),
	('CO', ' Completed'),
	('FA', 'Failed')
]

class Product(models.Model):
	name = models.CharField(max_length=100)
	category = models.CharField(max_length=100,choices=CATEGORIES)
	price = models.FloatField()

	def __str__(self):
		return self.name

class Order(models.Model):
	profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	price = models.FloatField()
	quantity = models.IntegerField()
	timestamp = models.DateTimeField(auto_now_add=True)
	status = models.CharField(max_length=100,choices=STATUS)

	def __str__(self):
		return str(self.timestamp)