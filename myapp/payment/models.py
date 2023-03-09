from django.db import models


# Create your models here.
class Payment(models.Model):
    amount = models.FloatField()
    method = models.CharField()
    completed = models.BooleanField()
    # user
    # ticket
