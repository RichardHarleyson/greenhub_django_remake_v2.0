#/home/greenhub/django/django_env/bin/env python
# -*- coding: utf-8 -*-
from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.index, name='electrocars'),
	path('add_veh', views.add_veh, name="add_veh"),
	path('add_veh_send', views.add_veh_send, name="add_veh_send"),
	path('upd_veh', views.upd_veh, name="upd_veh"),
	path('del_veh', views.del_veh, name="del_veh"),
]
