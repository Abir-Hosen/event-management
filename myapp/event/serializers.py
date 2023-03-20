from event.models import EventCategory, WhenEvent, WhereEvent, HowMuchEvent, SellingEvent, Event

from rest_framework import serializers


class EventCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EventCategory
        fields = ['id', 'name', 'description']


class WhenEventSerializer(serializers.HyperlinkedModelSerializer):
    event = serializers.PrimaryKeyRelatedField(queryset=Event.objects.all(), many=False)

    class Meta:
        model = WhenEvent
        fields = ['id', 'start_date', 'end_date', 'start_time', 'end_time', 'event']


class WhereEventSerializer(serializers.HyperlinkedModelSerializer):
    event = serializers.PrimaryKeyRelatedField(queryset=Event.objects.all(), many=False)

    class Meta:
        model = WhereEvent
        fields = ['id', 'name', 'description', 'event']


class HowMuchEventSerializer(serializers.HyperlinkedModelSerializer):
    event = serializers.PrimaryKeyRelatedField(queryset=Event.objects.all(), many=False)

    class Meta:
        model = HowMuchEvent
        fields = ['id', 'quantity', 'price', 'event']


class SellingEventSerializer(serializers.HyperlinkedModelSerializer):
    event = serializers.PrimaryKeyRelatedField(queryset=Event.objects.all(), many=False)

    class Meta:
        model = SellingEvent
        fields = ['id', 'refund', 'policy', 'terms_n_conditions', 'stripe_payment', 'event']


class EventSerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=EventCategory.objects.all(), many=False)

    class Meta:
        model = Event
        fields = ['id', 'title', 'published', 'description', 'category', 'status']
