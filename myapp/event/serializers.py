from event.models import EventCategory, WhenEvent, WhereEvent, HowMuchEvent, SellingEvent, Event

from rest_framework import serializers


class EventCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EventCategory
        fields = ['id', 'name', 'description']


class WhenEventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WhenEvent
        fields = ['id', 'name', 'description']


class WhereEventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WhereEvent
        fields = ['id', 'name', 'description']


class HowMuchEventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HowMuchEvent
        fields = ['id', 'name', 'description']


class SellingEventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SellingEvent
        fields = ['id', 'name', 'description']


class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'name', 'description']

