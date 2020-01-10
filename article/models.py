from django.db import models

class Article(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField("Name", max_length=30)
