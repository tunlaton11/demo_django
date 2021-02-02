from django.db import models

# Create your models here.
class Rating(models.Model):
    email = models.CharField(max_length=50)
    tel = models.CharField(max_length=15)
    comment = models.TextField(max_length=200)
    rating = models.IntegerField()