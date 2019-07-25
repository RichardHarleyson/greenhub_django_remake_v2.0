#/home/greenhub/django/django_env/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from .models import Vehicle, Vehicle_new
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt,csrf_protect

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
	vehicles = Vehicle_new.objects.all().filter(veh_status='Готов', record_status=True)
	return render(request, 'electrocars/add_veh.html', context={'vehicles' : vehicles})

def add_veh_send(request):
	myfile = request.FILES.get('veh_photo')
	fs = FileSystemStorage()
	filename = fs.save(myfile.name, myfile)
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

@csrf_exempt
def upd_veh(request):
	if len(request.FILES) != 0:
		myfile = request.FILES.get('veh_photo')
		fs = FileSystemStorage()
		filename = fs.save(myfile.name, myfile)
		print(filename)
		upd_veh = Vehicle_new.objects.all().filter(id = int(request.POST.get('veh_id'))).update(
			veh_photo = fs.url(filename),
			)
	upd_veh = Vehicle_new.objects.all().filter(id = int(request.POST.get('veh_id'))).update(
			veh_model = request.POST.get('veh_model'),
			# veh_photo = fs.url(filename),
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

@csrf_exempt
def del_veh(request):
	del_veh = Vehicle_new.objects.all().filter(id = int(request.POST.get('veh_id'))).update(
		veh_status = 'Не готов',
		record_status = False,
	)
	return HttpResponse(True)
