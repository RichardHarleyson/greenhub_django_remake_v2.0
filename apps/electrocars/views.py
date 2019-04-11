#/home/greenhub/django/django_env/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from .models import Vehicle
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

def index(request):
	car_list = Vehicle.objects.all().filter(veh_status=1)
	paginator = Paginator(car_list, 5)

	page = request.GET.get('page')
	cars = paginator.get_page(page)
	return render(request, 'electrocars/base_electrocars.html', context={'cars' : cars})
