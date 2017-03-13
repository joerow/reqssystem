from django.db import models


# Create your models here.

class Order(models.Model):
    equipment = models.CharField(max_length=500)
    date = models.DateField(null=True)
    tperiod = models.IntegerField


class Staff(models.Model):
    name = models.CharField(max_length=500)
    institution = models.CharField(max_length=500)

