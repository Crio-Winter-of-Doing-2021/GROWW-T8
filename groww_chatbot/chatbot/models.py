from django.db import models

# # Create your models here.
class FAQs(models.Model):
    question = models.CharField(max_length = 500)
    answer = models.CharField(max_length = 600)
    list_of_category = [
        ('Stk',"Stocks"),
        ('mf',"Mutual-funds"),
        ('gd',"gold"),
        ('fd',"Fix-Deposits"),
        ('profile',"Profile")
    ]
    category = models.CharField( choices = list_of_category, max_length=50)
