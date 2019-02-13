from django.db import models
import os
from django.conf import settings

class Vehicle(models.Model):
	veh_title = models.CharField(max_length=100)
	veh_comp = models.CharField(max_length=10, blank=True)
	veh_vin = models.CharField(max_length=30, unique=True)
	veh_year = models.CharField(max_length=12, blank=True)
	veh_mileage = models.CharField(max_length=20, blank=True)
	veh_color_in = models.CharField(max_length=30, blank=True)
	veh_color = models.CharField(max_length=30)
	veh_price = models.CharField(max_length=10)
	# veh_photo = models.CharField(max_length=250, blank=True)
	veh_photo = models.FileField(upload_to='greenhub_remake/static/img/vehicles/%Y/%m/%d/', blank=True)
	# veh_folder = models.CharField(max_length=350, blank=True)
	veh_battery = models.CharField(max_length=10, blank=True)
	veh_info = models.CharField(max_length=100, blank=True)
	veh_type = models.CharField(max_length=10)
	veh_status = models.PositiveSmallIntegerField(default=0)
	add_date = models.DateTimeField(auto_now_add=True)

	def full_name(self):
		return '{} {} {}'.format(self.veh_title, self.veh_comp, self.veh_year)

class Vehicle_photos(models.Model):
	veh_photo = models.CharField(max_length=250)
	veh_id = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='photos')
	type = models.PositiveSmallIntegerField(default=0)
