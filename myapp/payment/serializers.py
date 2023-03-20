from rest_framework import serializers
from payment.models import VolunteerStripePayment
from ticket.models import VolunteerTicket


class VolunteerStripePaymentSerializer(serializers.HyperlinkedModelSerializer):
    volunteer_ticket = serializers.PrimaryKeyRelatedField( queryset=VolunteerTicket.objects.all(), many=False)

    class Meta:
        model = VolunteerStripePayment
        fields = ['id', 'email', 'currency', 'purchased', 'volunteer_ticket']

