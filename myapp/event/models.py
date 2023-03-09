from django.db import models


# Create your models here.

class EventCategory(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    category = models.OneToOneField(EventCategory, on_delete=models.DO_NOTHING)


class WhereEvent(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    event = models.OneToOneField(Event, on_delete=models.DO_NOTHING)


class WhenEvent(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    event = models.OneToOneField(Event, on_delete=models.DO_NOTHING)


class HowMuchEvent(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    event = models.OneToOneField(Event, on_delete=models.DO_NOTHING)


class SellingEvent(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    event = models.OneToOneField(Event, on_delete=models.DO_NOTHING)


class Value(models.Model):
    name: models.CharField(max_length=200)
