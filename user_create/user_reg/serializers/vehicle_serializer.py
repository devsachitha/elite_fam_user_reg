from rest_framework import serializers
from ..models.vehicle import VehicleBrand
from ..models.vehicle import VehicleModel
from ..models.vehicle import Vehicle


# Vehicle Serializer
class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['vehicle_brand', 'vehicle_model', 'vehicle_reg_number']


# Vehicle Model Serializer
class VehicleModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleModel
        fields = ['name', 'vehicle_brand']


# Vehicle Brand Serializer
class VehicleBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleBrand
        fields = ['name']