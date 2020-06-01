from django.contrib.auth.models import User
from django.db import models


class Cars(models.Model):
    name = models.CharField(max_length=250)
    model = models.CharField(max_length=200)
    top_speed = models.IntegerField()
    user = models.ManyToManyField(User, related_name='user', blank=True)

    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    name = models.CharField(max_length=250)
    cars = models.ManyToManyField(Cars, related_name='manufacturer',blank=True)

    def __str__(self):
        return self.name


