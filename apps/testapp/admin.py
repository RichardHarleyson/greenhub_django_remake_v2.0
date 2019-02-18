from django.contrib import admin
from .models import Gdrive_vehicles

class MainAdmin(admin.ModelAdmin):
	list_display = (
		'id',
		'veh_title',
		'veh_vin',
		'veh_folder',
		'status'
	)

admin.site.register(Gdrive_vehicles, MainAdmin)
