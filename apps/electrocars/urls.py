#/home/greenhub/django/django_env/bin/env python
# -*- coding: utf-8 -*-
from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.index, name='electrocars')
]
