from django.db import models
from datetime import date
from django.utils import timezone


# Create your models here.

class EventCategory(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    published = models.BooleanField(default=False)
    status = models.CharField(max_length=10, default='Draft')
    category = models.ForeignKey(EventCategory, on_delete=models.DO_NOTHING)


class WhereEvent(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(default='')
    event = models.OneToOneField(Event, on_delete=models.DO_NOTHING)


class WhenEvent(models.Model):
    start_date = models.DateField(default=date.today)
    end_date = models.DateField(default=date.today)
    start_time = models.TimeField(default=timezone.now)
    end_time = models.TimeField(default=timezone.now)
    event = models.OneToOneField(Event, on_delete=models.DO_NOTHING)


class HowMuchEvent(models.Model):
    quantity = models.IntegerField(default=1)
    price = models.FloatField(default=1)
    event = models.OneToOneField(Event, on_delete=models.DO_NOTHING)


class SellingEvent(models.Model):
    refund = models.BooleanField(default=False)
    policy = models.TextField(default='', null=True)
    terms_n_conditions = models.TextField(default='', null=True)
    stripe_payment = models.BooleanField(default=True)
    event = models.OneToOneField(Event, on_delete=models.DO_NOTHING)


class Value(models.Model):
    name: models.CharField(max_length=200)
