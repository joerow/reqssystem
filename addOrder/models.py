from django.db import models


# Create your models here.

class Order(models.Model):

    # Fields
    equipment = models.CharField(max_length=500, help_text="Type the equipment name")
    date = models.DateField(null=True, help_text="Types the date in format dd/mm")
    tperiod = models.IntegerField(help_text="Enter the teaching period")

    # Meta
    class Meta:
        ordering = ["equipment"]

    # methods


class Staff(models.Model):

    # Fields
    name = models.CharField(max_length=500)
    institution = models.CharField(max_length=500)

