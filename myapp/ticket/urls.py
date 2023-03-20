from django.urls import path, include
from rest_framework.routers import DefaultRouter
from ticket import views

router = DefaultRouter()
router.register(r'tickets', views.TicketViewSet, basename='tickets')
router.register(r'ticket-type', views.TicketTypeViewSet, basename='ticket-type')
router.register(r'volunteer-ticket', views.VolunteerTicketViewSet, basename='volunteer-ticket')

urlpatterns = [
    path('', include(router.urls)),
]
