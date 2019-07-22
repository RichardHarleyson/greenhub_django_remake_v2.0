#/home/greenhub/django/django_env/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Vehicle, Vehicle_photos, Vehicle_new

def Готово(modeladmin, request, queryset):
	queryset.update(veh_status=1)

def Не_Готово(modeladmin, request, queryset):
	queryset.update(veh_status=0)

class VehiclePictureInline(admin.TabularInline):
	model = Vehicle_photos
	fields = ['veh_photo']

class MainAmdmin(admin.ModelAdmin):
	list_display = (
		'veh_title',
		'veh_comp',
		'veh_vin',
		'veh_year',
		'veh_mileage',
		'veh_price',
		'veh_photo',
		'veh_type',
		'veh_status',
		'id',
		'add_date',
		)
	inlines = [VehiclePictureInline,]
	actions = [Готово, Не_Готово]

class NewVehicle(admin.ModelAdmin):
	list_display = (
	'id',
	'veh_model',
	'veh_photo',
	'veh_type',
	'veh_status',
	'add_date',
	)

admin.site.register(Vehicle, MainAmdmin)
admin.site.register(Vehicle_new, NewVehicle)
