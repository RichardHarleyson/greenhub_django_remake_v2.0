#/home/greenhub/django/django_env/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin
from django.urls import path, include
from . import views
import apps.clients.views as clients_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	# Admin
    path('admin/', admin.site.urls),
	# Core pages
	path('', views.index, name='index'),
	path('contacts/', views.contacts, name='contacts'),
	path('charger_map/', views.charger_map, name='charger_map'),
	# Apps pages
	path('electrocars/', include('apps.electrocars.urls')),
	path('electromoto/', include('apps.electromoto.urls')),
	# path('testapp/', include('apps.testapp.urls')),
	path('testdrive_form', clients_views.testdrive_form, name='testdrive_form'),
	path('callme_form', clients_views.callme_form, name='callme_form'),

]
