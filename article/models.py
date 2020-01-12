from django.db import models

class Article(models.Model):
    name = models.CharField("Name", max_length=30)
