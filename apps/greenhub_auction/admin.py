from django.contrib import admin
from .models import Client_Task

# Register your models here.

class MainAdmin(admin.ModelAdmin):
	list_display = (
	'veh_model',
	'veh_type',
	'veh_state',
	'tariff',
	'budget',
	'add_date',
	)

admin.site.register(Client_Task, MainAdmin)
