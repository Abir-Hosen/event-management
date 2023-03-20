from rest_framework import serializers
from ticket.models import TicketType, VolunteerTicket, Ticket
from event.models import Event
from user.models import User


class TicketTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TicketType
        fields = ['id', 'name', 'is_volunteer_type', 'discount_percent', 'description']


class VolunteerTicketSerializer(serializers.HyperlinkedModelSerializer):
    event = serializers.PrimaryKeyRelatedField(queryset=Event.objects.all(), many=False)
    ticket_type = serializers.PrimaryKeyRelatedField(queryset=TicketType.objects.all(), many=False)

    class Meta:
        model = VolunteerTicket
        fields = ['id', 'name', 'event', 'ticket_type', 'agreement_template', 'introduction_template', 'whs_template',
                  'link', 'ticket_template', 'terms_n_condition', 'note', 'public_key', 'secret_key']


class TicketSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=False)
    volunteer_ticket = serializers.PrimaryKeyRelatedField(queryset=VolunteerTicket.objects.all(), many=False)

    class Meta:
        model = Ticket
        fields = ['id', 'stripe_id', 'user', 'volunteer_ticket']
