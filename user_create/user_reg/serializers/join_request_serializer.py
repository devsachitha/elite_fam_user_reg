from rest_framework import serializers
from ..models.join_request import JoinRequest


class JoinRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = JoinRequest
        fields = ['first_name', 'last_name', 'applied_date', 'status', 'city', 'province', 'vehicle_reg']