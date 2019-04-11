#/home/greenhub/django/django_env/bin/env python
# -*- coding: utf-8 -*-
from django.db import models

class Client_Task(models.Model):
	veh_type_choice = [('EV', 'EV'),('DVS','ДВС')]
	veh_state_choice = [('hit','Битая'),('fine','Целая')]
	tariff_choice = [('500','500'),('700','700'),('1000','1000')]
	veh_type = models.CharField(max_length=5, choices=veh_type_choice, default=veh_type_choice[0])
	veh_state = models.CharField(max_length=10, choices=veh_state_choice, default=veh_state_choice[0])
	tariff = models.CharField(max_length=5, choices=tariff_choice, default=tariff_choice[1])
	budget = models.CharField(max_length=20, blank=False)
	veh_model = models.CharField(max_length=50, blank=False)
	veh_comp = models.CharField(max_length=10, blank=True)
	veh_year = models.CharField(max_length=12, blank=True)
	veh_mileage = models.CharField(max_length=20, blank=True)
	veh_color_in = models.CharField(max_length=30, blank=True)
	veh_color = models.CharField(max_length=30)
	add_date = models.DateTimeField(auto_now_add=True)

def full_name(self):
	return '{} {} {}'.format(self.veh_model, self.veh_comp, self.veh_year)
