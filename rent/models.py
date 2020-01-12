from django.db import models
from article.models import Article
from customer.models import Customer

class Rent(models.Model):
    name = models.CharField("Name", max_length=30)
    article = models.ForeignKey(Article,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
