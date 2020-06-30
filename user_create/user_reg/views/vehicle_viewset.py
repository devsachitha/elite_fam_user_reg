from rest_framework import viewsets
from ..serializers.vehicle_serializer import VehicleSerializer
from ..serializers.vehicle_serializer import VehicleBrandSerializer
from ..serializers.vehicle_serializer import VehicleModelSerializer
from rest_framework.authentication import TokenAuthentication

from ..models.vehicle import Vehicle
from ..models.vehicle import VehicleModel
from ..models.vehicle import VehicleBrand


class VehicleViewSet(viewsets.ModelViewSet):
    serializer_class = VehicleSerializer
    queryset = Vehicle.objects.all()
    authentication_classes = (TokenAuthentication,)


class VehicleModelViewSet(viewsets.ModelViewSet):
    serializer_class = VehicleModelSerializer
    queryset = VehicleModel.objects.all()
    authentication_classes = (TokenAuthentication,)


class VehicleBrandViewSet(viewsets.ModelViewSet):
    serializer_class = VehicleBrandSerializer
    queryset = VehicleBrand.objects.all()
    authentication_classes = (TokenAuthentication,)

