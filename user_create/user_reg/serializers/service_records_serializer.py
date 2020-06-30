from rest_framework import serializers
from ..models.service_records import ServiceRecords
from ..models.service_records import ServiceRecordLines


# Service record lines serializer
class ServiceRecordLinesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceRecordLines
        fields = ['service_item', 'service_description']


# Service Records serializer
class ServiceRecordsSerializer(serializers.ModelSerializer):
    service_record_lines = ServiceRecordLinesSerializer(many=True)

    class Meta:
        model = ServiceRecords
        fields = ['vehicle', 'vehicle_mileage', 'service_date','service_record_lines']
