from django.shortcuts import render

# Create your views here.
from .models import Volunteer
from .serializers import VolunteerSerializer
from django.http import HttpResponse

from rest_framework import viewsets, permissions

# def index(request):
#     print(request)
#     return HttpResponse("Hello from volunteers")

class VolunteerViewSet(viewsets.ModelViewSet):
    queryset = Volunteer.objects.all()
    serializer_class = VolunteerSerializer
    permission_classes = [permissions.IsAuthenticated]