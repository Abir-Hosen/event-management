from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from payment.models import VolunteerStripePayment
from event.models import HowMuchEvent
from event.serializers import HowMuchEventSerializer
from payment.serializers import VolunteerStripePaymentSerializer
from ticket.models import VolunteerTicket, TicketType
from ticket.serializers import VolunteerTicketSerializer, TicketTypeSerializer
from rest_framework.response import Response
import stripe
import json


# Create your views here.

class VolunteerStripePaymentViewSet(viewsets.ModelViewSet):
    queryset = VolunteerStripePayment.objects.all()
    serializer_class = VolunteerStripePaymentSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request):
        volunteer_ticket_by_id = VolunteerTicket.objects.get(id=request.data['volunteer_ticket'])
        stripe.api_key = volunteer_ticket_by_id.secret_key
        serializer = VolunteerStripePaymentSerializer(data=request.data)

        how_much = HowMuchEvent.objects.get(event=volunteer_ticket_by_id.event_id)
        ticket_type = TicketType.objects.get(id=volunteer_ticket_by_id.ticket_type_id)
        amount = int((how_much.price - (how_much.price * (ticket_type.discount_percent / 100))) * 100)

        try:
            intent = stripe.PaymentIntent.create(
                amount=amount,
                currency='aud',
                automatic_payment_methods={
                    'enabled': True,
                },
            )
            if serializer.is_valid():
                serializer.save()
                return Response({'data': serializer.data, 'clientSecret': intent['client_secret'], 'amount': amount},
                                status=status.HTTP_201_CREATED)
            else:
                Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
