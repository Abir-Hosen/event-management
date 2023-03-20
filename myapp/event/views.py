from django.shortcuts import render
from rest_framework import viewsets, permissions
# from rest_framework.pagination import pagination_class
from event.models import EventCategory, WhenEvent, WhereEvent, HowMuchEvent, SellingEvent, Event
from event.serializers import EventSerializer, EventCategorySerializer, WhenEventSerializer, WhereEventSerializer, \
    HowMuchEventSerializer, SellingEventSerializer


# Create your views here.
class EventCategoryViewSet(viewsets.ModelViewSet):
    queryset = EventCategory.objects.all()
    serializer_class = EventCategorySerializer
    permission_classes = [permissions.AllowAny]
    # pagination_class = None

    # def get_queryset(self):
    #     page = self.request.GET.get('pages', None)
    #     if page is None:
    #         pagination_class = None
    #         self.queryset = EventCategory.objects.all()
    #     else:
    #         self.queryset = EventCategory.objects.all()
    #     return self.queryset


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.AllowAny]


class WhereEventViewSet(viewsets.ModelViewSet):
    queryset = WhereEvent.objects.all()
    serializer_class = WhereEventSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        event = self.request.GET.get('event', None)
        if event is None:
            self.queryset = WhereEvent.objects.all()
        else:
            self.queryset = WhereEvent.objects.filter(event=event)
        return self.queryset


class WhenEventViewSet(viewsets.ModelViewSet):
    queryset = WhenEvent.objects.all()
    serializer_class = WhenEventSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        event = self.request.GET.get('event', None)
        if event is None:
            self.queryset = WhenEvent.objects.all()
        else:
            self.queryset = WhenEvent.objects.filter(event=event)
        return self.queryset


class HowMuchEventViewSet(viewsets.ModelViewSet):
    queryset = HowMuchEvent.objects.all()
    serializer_class = HowMuchEventSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        event = self.request.GET.get('event', None)
        if event is None:
            self.queryset = HowMuchEvent.objects.all()
        else:
            self.queryset = HowMuchEvent.objects.filter(event=event)
        return self.queryset


class SellingEventViewSet(viewsets.ModelViewSet):
    queryset = SellingEvent.objects.all()
    serializer_class = SellingEventSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        event = self.request.GET.get('event', None)
        if event is None:
            self.queryset = SellingEvent.objects.all()
        else:
            self.queryset = SellingEvent.objects.filter(event=event)
        return self.queryset
