from django.contrib import admin
from .models import Vehicle, Vehicle_photos


class VehiclePictureInline(admin.TabularInline):
	model = Vehicle_photos
	fields = ['veh_photo']

class MainAmdmin(admin.ModelAdmin):
	list_display = (
		'id',
		'veh_title',
		'veh_comp',
		'veh_vin',
		'veh_year',
		'veh_mileage',
		'veh_price',
		'veh_folder',
		'veh_type',
		'veh_status',
		'add_date',
		)
	inlines = [VehiclePictureInline,]

admin.site.register(Vehicle, MainAmdmin)
