#/home/greenhub/django/django_env/bin/env python
# -*- coding: utf-8 -*-
from django.db import models

class Gdrive_vehicles(models.Model):
	veh_title = models.CharField(max_length=100, blank=True)
	veh_vin = models.CharField(max_length=50, blank=False, unique=True)
	veh_folder = models.CharField(max_length=250, blank=True)
	status = models.PositiveSmallIntegerField(default=0)
