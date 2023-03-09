from django.shortcuts import render
from rest_framework import viewsets, permissions
from event.models import EventCategory, WhenEvent, WhereEvent, HowMuchEvent, SellingEvent, Event
from event.serializers import EventSerializer, EventCategorySerializer, WhenEventSerializer, WhereEventSerializer, \
    HowMuchEventSerializer, SellingEventSerializer


# Create your views here.
class EventCategoryViewSet(viewsets.ModelViewSet):
    queryset = EventCategory.objects.all()
    serializer_class = EventCategorySerializer
    permission_classes = [permissions.AllowAny]


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.AllowAny]


class WhereEventViewSet(viewsets.ModelViewSet):
    queryset = WhereEvent.objects.all()
    serializer_class = WhereEventSerializer
    permission_classes = [permissions.AllowAny]


class WhenEventViewSet(viewsets.ModelViewSet):
    queryset = WhenEvent.objects.all()
    serializer_class = WhenEventSerializer
    permission_classes = [permissions.AllowAny]


class HowMuchEventViewSet(viewsets.ModelViewSet):
    queryset = HowMuchEvent.objects.all()
    serializer_class = HowMuchEventSerializer
    permission_classes = [permissions.AllowAny]


class SellingEventViewSet(viewsets.ModelViewSet):
    queryset = SellingEvent.objects.all()
    serializer_class = SellingEventSerializer
    permission_classes = [permissions.AllowAny]

