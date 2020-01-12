from django.db import models

class Customer(models.Model):
    name = models.CharField("Name", max_length=30)
