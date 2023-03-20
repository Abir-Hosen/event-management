from django.db import models
from ticket.models import VolunteerTicket


# Create your models here.
class Payment(models.Model):
    email = models.FloatField(max_length=100)
    # amount = models.FloatField()
    # method = models.CharField()
    # completed = models.BooleanField()
    # user
    # ticket


class VolunteerStripePayment(models.Model):
    email = models.CharField(max_length=100, default='')
    currency = models.CharField(max_length=100, default='aud')
    purchased = models.BooleanField(default=False)
    volunteer_ticket = models.ForeignKey(VolunteerTicket, on_delete=models.DO_NOTHING)

    # completed = models.BooleanField()
    # user
    # ticket
