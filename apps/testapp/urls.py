#/home/greenhub/django/django_env/bin/env python
# -*- coding: utf-8 -*-
from django.urls import path, include
from . import views

urlpatterns = [
	path('grab_vehs_kiev', views.grab_vehs_kiev, name='grab_vehs_kiev'),
	path('grab_vehs_salon', views.grab_vehs_salon, name='grab_vehs_salon'),
	path('grab_photos', views.grab_photos, name='grab_photos'),
]
