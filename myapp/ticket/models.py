from django.db import models


# Create your models here.
class TicketType(models.Model):
    name = models.CharField(max_length=100)
    is_volunteer_type = models.BooleanField(default=False)
    discount_percent = models.IntegerField()
    description = models.CharField(max_length=3000)


class Ticket(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=3000)
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
