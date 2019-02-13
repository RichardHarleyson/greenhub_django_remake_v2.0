from django.contrib import admin
from .models import Vehicle

class MainAmdmin(admin.ModelAdmin):
	list_display = (
		'veh_title',
		'veh_comp',
		'veh_vin',
		'veh_year',
		'veh_mileage',
		'veh_price',
		'veh_type',
		'veh_status',
		'add_date',
		)

admin.site.register(Vehicle, MainAmdmin)
