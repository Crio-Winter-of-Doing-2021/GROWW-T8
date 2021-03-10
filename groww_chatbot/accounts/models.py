from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User,on_delete=CASCADE)
	name = models.CharField(max_length=100,null=True)
	dob = models.DateField(null=True)
	kyc = models.BooleanField(default=False)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.user)