from django.urls import path, include
from rest_framework.routers import DefaultRouter
from payment.views import VolunteerStripePaymentViewSet

router = DefaultRouter()
router.register(r'volunteer-stripe-payment', VolunteerStripePaymentViewSet, basename='volunteer-stripe-payment')

urlpatterns = [
    path('', include(router.urls)),
]
