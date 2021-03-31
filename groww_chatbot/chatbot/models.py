from django.db import models

# Create your models here.
class FAQs(models.Model):
    id = models.AutoField()
    question = models.CharField(max_length = 500)
    answer = models.CharField(max_length = 600)
    category = [

    ]
    