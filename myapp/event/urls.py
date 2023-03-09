from django.urls import path, include
from rest_framework.routers import DefaultRouter
from event.views import EventViewSet, WhenEventViewSet, WhereEventViewSet, HowMuchEventViewSet, EventCategoryViewSet, \
    SellingEventViewSet

router = DefaultRouter()
router.register(r'', EventViewSet, basename='event')
router.register(r'event-category', EventCategoryViewSet, basename='event-category')
router.register(r'where-event', WhereEventViewSet, basename='where-event')
router.register(r'when-event', WhenEventViewSet, basename='when-event')
router.register(r'how-much-event', HowMuchEventViewSet, basename='how-much-event')
router.register(r'selling-event', SellingEventViewSet, basename='selling-event')

urlpatterns = [
    path('', include(router.urls)),
]
