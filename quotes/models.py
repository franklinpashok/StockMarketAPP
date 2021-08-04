from django.db import models
# Create your models here.
class Stock(models.Model):
# this is a global attribute for this class
    ticker = models.CharField(max_length=10)
# Intantiate the class
    def __str__(self):
        return self.ticker
