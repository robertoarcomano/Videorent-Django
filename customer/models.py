from django.db import models

class Customer(models.Model):
    name = models.CharField("Name", max_length=30)
    def init(N):
        customers = Customer.objects.filter(name__contains='Customer_')
        customers.delete()
        customers = []
        for i in range(1,N+1):
            customer = Customer(name="Customer_"+str(i))
            customer.save()
            customers.append(customer);
        return customers
