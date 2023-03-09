
from rest_framework import serializers
from ticket.models import TicketType

class TicketTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TicketType
        fields = ['id', 'name', 'is_volunteer_type', 'discount_percent', 'description']
