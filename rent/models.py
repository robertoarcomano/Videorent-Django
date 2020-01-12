from django.db import models
from article.models import Article
from customer.models import Customer

class Rent(models.Model):
    name = models.CharField("Name", max_length=30)
    article = models.ForeignKey(Article,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)

    def init(articles, customers):
        rents = Rent.objects.filter(name__contains='Rent_')
        rents.delete()
        rents = []
        i = 1
        for article in articles:
            for customer in customers:
                rents.append(Rent(name="Rent_"+str(i),article=article,customer=customer))
                i += 1
        Rent.objects.bulk_create(rents)
