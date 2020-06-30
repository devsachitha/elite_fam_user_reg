from django.db import models


class VehicleBrand(models.Model):
    """Create Vehicle Brand Here"""
    name = models.CharField(null=False, max_length=50)

    def __str__(self):
        return self.name


class VehicleModel(models.Model):
    """Vehicle Models create in here"""
    name = models.CharField(null=False, max_length=50)
    vehicle_brand = models.ForeignKey(VehicleBrand, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Vehicle(models.Model):
    """Register The vehicle Under here"""
    vehicle_brand = models.ForeignKey(VehicleBrand, on_delete=models.CASCADE, null=False)
    vehicle_model = models.ForeignKey(VehicleModel, on_delete=models.CASCADE, null=False)
    vehicle_reg_number = models.CharField(null=False, max_length=20)

    def __str__(self):
        return self.vehicle_reg_number



