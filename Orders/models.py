from django.db import models

# Create your models here.

class Order(models.Model):

    date_ordered = models.DateField()
    