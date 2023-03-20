from django.db import models
from event.models import Event
from user.models import User


# Create your models here.
class TicketType(models.Model):
    name = models.CharField(max_length=100)
    is_volunteer_type = models.BooleanField(default=False)
    discount_percent = models.IntegerField()
    description = models.CharField(max_length=3000)


class VolunteerTicket(models.Model):
    name = models.CharField(max_length=100)
    event = models.ForeignKey(Event, on_delete=models.DO_NOTHING)
    ticket_type = models.ForeignKey(TicketType, on_delete=models.DO_NOTHING)
    agreement_template = models.TextField(default='')
    introduction_template = models.TextField(default='')
    whs_template = models.TextField(default='')
    link = models.CharField(max_length=1000)
    ticket_template = models.TextField(default='')
    terms_n_condition = models.TextField(default='')
    note = models.TextField(default='')
    public_key = models.TextField(default='')
    secret_key = models.TextField(default='')

    # event
    # ticket_category
    # discount[]


# class Discount(models.Model):
#     name = models.CharField(max_length=100)
#     code = models.CharField(max_length=50)
#     discount_amount = models.FloatField()
#     discount_percent = models.FloatField()


class TicketCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=3000)


class Ticket(models.Model):
    stripe_id = models.TextField()
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    volunteer_ticket = models.ForeignKey(VolunteerTicket, on_delete=models.DO_NOTHING, null=True)
