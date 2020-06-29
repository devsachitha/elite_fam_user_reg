from django.contrib import admin
from .models.join_request import JoinRequest
from .models.vehicle import VehicleBrand
from .models.vehicle import VehicleModel


# Register your models here.
@admin.register(JoinRequest)
class JoinrequestAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']
    list_filter = ['applied_date', 'applied_date']
    search_fields = ['first_name', 'last_name']


admin.site.register(VehicleBrand)
admin.site.register(VehicleModel)

