from django.db import models

# categories = [
#     ('ST',"Stocks"),
#     ('MF',"Mutual funds"),
#     ('GO',"gold"),
#     ('FD',"Fixed Deposits"),
#     ('AC',"Account"),
#     ('OR','Orders'),
#     ('KYC','KYC'),
#     ('LI','Logged In')
# ]

# # Create your models here.
class FAQ(models.Model):
    question = models.CharField(max_length = 500)
    answer = models.CharField(max_length = 600)
    usedFotBot = models.BooleanField(default=False)

    def __str__(self):
        return self.question

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class CategoryMap(models.Model):
    question = models.ForeignKey(FAQ, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
