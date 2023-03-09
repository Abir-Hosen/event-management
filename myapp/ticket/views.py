from django.shortcuts import render
from rest_framework import viewsets, permissions
from ticket.models import TicketType
from ticket.serializers import TicketTypeSerializer

# Create your views here.
class TicketTypeViewSet(viewsets.ModelViewSet):
    queryset = TicketType.objects.all()
    serializer_class = TicketTypeSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        is_volunteer_type = self.request.GET.get('is_volunteer_type', None)
        if is_volunteer_type is None:
            self.queryset = TicketType.objects.all()
        else:
            self.queryset = TicketType.objects.filter(is_volunteer_type=is_volunteer_type)
        return self.queryset
