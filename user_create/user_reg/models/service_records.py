from django.db import models
from . import vehicle


class ServiceRecords(models.Model):
    """All vehicle service records create in here"""
    vehicle = models.ForeignKey(vehicle.Vehicle, on_delete=models.CASCADE, null=False)
    vehicle_mileage = models.CharField(max_length=10, null=False)
    service_date = models.DateField()

    def __str__(self):
        return self.service_date


class ServiceRecordLines(models.Model):
    """Service record lines"""
    service_record = models.ForeignKey(ServiceRecords, on_delete=models.CASCADE, null=False)
    service_item = models.CharField(max_length=100, null=False)
    service_description = models.TextField(null=True)

    def __str__(self):
        return self.service_item
