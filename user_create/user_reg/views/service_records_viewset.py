from rest_framework import viewsets
from ..serializers.service_records_serializer import ServiceRecordsSerializer
from ..serializers.service_records_serializer import ServiceRecordLinesSerializer
from ..models.service_records import ServiceRecords
from ..models.service_records import ServiceRecordLines
from rest_framework.authentication import TokenAuthentication


class ServiceRecordsViewSet(viewsets.ModelViewSet):
    serializer_class = ServiceRecordsSerializer
    queryset = ServiceRecords.objects.all()
    authentication_classes = (TokenAuthentication,)


class ServiceRecordLinesViewSet(viewsets.ModelViewSet):
    serializer_class = ServiceRecordLinesSerializer
    queryset = ServiceRecordLines.objects.all()
    authentication_classes = (TokenAuthentication,)
