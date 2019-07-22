#/home/greenhub/django/django_env/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from .models import Vehicle, Vehicle_new
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.conf import settings
from django.core.files.storage import FileSystemStorage

def index(request):
	car_list = Vehicle.objects.all().filter(veh_status=1)
	vehicles = Vehicle_new.objects.all().filter(veh_status='Готов' , record_status=True)
	paginator = Paginator(car_list, 5)

	page = request.GET.get('page')
	cars = paginator.get_page(page)
	return render(request, 'electrocars/base_electrocars.html', context={
		'cars' : cars,
		'vehicles' : vehicles
	})

def add_veh(request):
	return render(request, 'electrocars/add_veh.html', context={})

def add_veh_send(request):
	myfile = request.FILES.get('veh_photo')
	fs = FileSystemStorage()
	filename = fs.save(myfile.name, myfile)
	# uploaded_file_url = fs.url(filename)
	new_vehicle = Vehicle_new.objects.create(
	veh_model = request.POST.get('veh_model'),
	veh_photo = fs.url(filename),
	veh_year = request.POST.get('veh_year'),
	veh_mileage = request.POST.get('veh_mileage'),
	veh_color_in = request.POST.get('veh_color_in'),
	vah_color = request.POST.get('veh_color'),
	veh_price = request.POST.get('veh_price'),
	veh_type = request.POST.get('veh_type'),
	veh_status = request.POST.get('veh_status'),
	veh_incomming_date = request.POST.get('veh_incomming_date'),
	)
	return HttpResponse(True)
