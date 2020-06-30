from django.urls import path, include
from . import views
from rest_framework import routers
from .views.join_request_viewset import JoinRequestViewSet
from .views.service_records_viewset import ServiceRecordsViewSet
from .views.service_records_viewset import ServiceRecordLinesViewSet
from .views.vehicle_viewset import VehicleBrandViewSet
from .views.vehicle_viewset import VehicleModelViewSet
from .views.vehicle_viewset import VehicleViewSet

router = routers.DefaultRouter()
router.register('join_request', JoinRequestViewSet)
router.register('vehicle', VehicleViewSet)
router.register('services', ServiceRecordsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
