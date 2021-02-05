from django.db import models

# Create your models here.
class Rating(models.Model):
    email = models.CharField(max_length=50)
    tel = models.CharField(max_length=15)
    comment = models.TextField(max_length=200)
    rating = models.IntegerField()


class Member(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    nickname = models.CharField(max_length=10)