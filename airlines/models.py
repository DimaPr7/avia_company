from django.contrib.auth.models import AbstractUser
from django.db import models


class Crew(models.Model):
    number = models.IntegerField()
    rate = models.IntegerField()


class Plane(models.Model):
    plane_model = models.CharField(max_length=15)
    plane_type = models.CharField(max_length=15)
    range_of_flight = models.IntegerField()
    crew = models.ForeignKey(Crew, on_delete=models.CASCADE,
                             related_name='planes')


class Order(models.Model):
    number = models.IntegerField()
    price = models.IntegerField()
    status = models.CharField(max_length=10)
    flight = models.ManyToManyField(Plane, related_name='orders')


class Client(AbstractUser):
    passport_number = models.CharField(max_length=8)
    pass
