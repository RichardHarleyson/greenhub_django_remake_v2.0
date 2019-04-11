#/home/greenhub/django/django_env/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from .models import Gdrive_vehicles
from apps.electrocars.models import Vehicle, Vehicle_photos
# Googledrive modules
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from oauth2client import file, client, tools
from apiclient.discovery import build
from httplib2 import Http


credentials_path = 'C://Python64//greenhub_pydrive//credentials.json'
client_secret_path = 'C://Python64//greenhub_pydrive//client_secret.json'
client_json_path = 'C://Python64//greenhub_pydrive//client_secret_.json'
access_email = 'C://Python64//greenhub_pydrive//access_email.json'

def grab_vehs_kiev(request):
	# Setup the Drive v2 API
	SCOPES = 'https://www.googleapis.com/auth/drive.metadata.readonly'
	store = file.Storage(credentials_path)
	creds = store.get()
	if not creds or creds.invalid:
	    flow = client.flow_from_clientsecrets(client_secret_path, SCOPES)
	    creds = tools.run_flow(flow, store)
	service = build('drive', 'v2', http=creds.authorize(Http()))
	# Подключаемся к google sheets
	scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
	creds = ServiceAccountCredentials.from_json_keyfile_name(client_json_path, scope)
	client = gspread.authorize(creds)
	# Подключаемся к листу
	# try:
	sheet1 = client.open_by_key('1nzwOMZIHoHFhU-VneJUWMPFjI03b-lXVPoUP9QzF1io').worksheet('Наявність')
	# except:
	# 	return HttpResponse('Permission denied!')
	sheet_records = sheet1.get_all_records()
	for record in sheet_records:
		# Проверяем доступно ли авто
		if str(record['Марка авто']) == '':
			continue
		if str(record['Статус']) != '' and  str(record['Статус']) != 'Готова':
			continue
		if(str(record['Бронювання']) != '' and str(record['Бронювання']) != 'Акція'):
			continue
		# Получаем ссылку на ресурс с фото
		hplink = sheet1.find(str(record['VIN']))
		hplink = sheet1.acell('D%s'%str(hplink.row),'FORMULA').value
		hplink_dir = hplink.replace('=HYPERLINK("','')
		veh_folder = hplink_dir.replace('";"%s")'%str(record['VIN']),'')
		# Формируем запись в таблице
		new_vehicle = Vehicle(
			veh_title = '{} {} {}'.format(str(record['Марка авто']), str(record['Комплектація']), str(record['Мод рік'])),
			veh_comp = str(record['Комплектація']),
			veh_vin = str(record['VIN']),
			veh_year = str(record['Мод рік']),
			veh_mileage = str(record['пробіг(км)']).replace('\xa0',''),
			veh_color_in = str(record['салон']),
			veh_color = str(record['салон']),
			veh_price = str(record['Ціна в салоні']).replace('\xa0',''),
			veh_folder = veh_folder,
			veh_photo = '',
			veh_battery = str(record['SOH']),
			veh_info = '',
			veh_type = 'dealler',
			veh_status = 0,
			)
		try:
			new_vehicle.save()
		except:
			print('Could not save %s record. Check if there is one already'%str(record['VIN']))
			continue
		print('Finished with %s'%str(record['VIN']))
		del(new_vehicle)
	return HttpResponse("<h1>Vehicles has been grabbed successfully</h1>")

def grab_vehs_salon(request):
	# Setup the Drive v2 API
	SCOPES = 'https://www.googleapis.com/auth/drive.metadata.readonly'
	store = file.Storage(credentials_path)
	creds = store.get()
	if not creds or creds.invalid:
	    flow = client.flow_from_clientsecrets(client_secret_path, SCOPES)
	    creds = tools.run_flow(flow, store)
	service = build('drive', 'v2', http=creds.authorize(Http()))
	# Подключаемся к google sheets
	scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
	creds = ServiceAccountCredentials.from_json_keyfile_name(access_email, scope)
	client = gspread.authorize(creds)
	# Подключаемся к листу
	# try:
	sheet1 = client.open_by_key('17V5kmDw1pTouSu_yiqW955OAQ9x968uH_NPwfjoj61A').worksheet('Main')
	# except:
	# 	return HttpResponse('Permission denied!')
	sheet_records = sheet1.get_all_records()
	for record in sheet_records:
		# Проверяем доступно ли авто
		# if str(record['Марка авто']) == '':
		# 	continue
		# if str(record['Статус']) != '' and  str(record['Статус']) != 'Готова':
		# 	continue
		# if(str(record['Бронювання']) != '' and str(record['Бронювання']) != 'Акція'):
		# 	continue
		# Получаем ссылку на ресурс с фото
		# hplink = sheet1.find(str(record['VIN']))
		# hplink = sheet1.acell('D%s'%str(hplink.row),'FORMULA').value
		# hplink_dir = hplink.replace('=HYPERLINK("','')
		# veh_folder = hplink_dir.replace('";"%s")'%str(record['VIN']),'')
		# veh_folder = str(record['Фото'])
		# Формируем запись в таблице
		new_vehicle = Vehicle(
			veh_title = '{} {} {}'.format(str(record['Марка авто']), str(record['Комплектация']), str(record['Год'])),
			veh_comp = str(record['Комплектация']),
			veh_vin = str(record['VIN']),
			veh_year = str(record['Год']),
			veh_mileage = str(record['Пробег']).replace('\xa0',''),
			veh_color_in = str(record['Салон']),
			veh_color = str(record['Кузов']),
			veh_price = str(record['Цена ($)']).replace('\xa0',''),
			veh_folder = str(record['Фото']),
			veh_photo = '',
			veh_battery = str(record['Батарея']),
			veh_info = '',
			veh_type = 'salon',
			veh_status = 0,
			)
		try:
			new_vehicle.save()
		except:
			print('Could not save %s record. Check if there is one already'%str(record['VIN']))
			continue
		print('Finished with %s'%str(record['VIN']))
		del(new_vehicle)
	return HttpResponse("Машины загружены. Нужно выставить фото")


def grab_photos(request):
	# Выбираем все записи для которых не собраны фоток
	veh_list = Vehicle.objects.all().filter(veh_status=0)
	for record in veh_list:
		if 'http' in record.veh_folder:
			# Проверяем на тип ссылки
			if 'google' in record.veh_folder:
				# обрабатываем гугл диск
				if 'id' in record.veh_folder:
					pass
				if 'folder' in record.veh_folder:
					pass
			if 'manheim' in record.veh_folder:
				# обрабатываем манхейм
				pass
			if 'copart' in record.veh_folder:
				# обрабатываем копарт
				pass
			if 'iaai' in record.veh_folder:
				# обрабатываем iaai
				pass

	return HttpResponse('<h1>Everything seems fine</h1>')
# ================================================

"""
	# Setup the Drive v2 API
	SCOPES = 'https://www.googleapis.com/auth/drive.metadata.readonly'
	store = file.Storage(credentials_path)
	creds = store.get()
	if not creds or creds.invalid:
	    flow = client.flow_from_clientsecrets(client_secret_path, SCOPES)
	    creds = tools.run_flow(flow, store)
	service = build('drive', 'v2', http=creds.authorize(Http()))

	# Подключаемся к google sheets
	scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
	creds = ServiceAccountCredentials.from_json_keyfile_name(client_json_path, scope)
	client = gspread.authorize(creds)
	sheet1 = client.open_by_key('1nzwOMZIHoHFhU-VneJUWMPFjI03b-lXVPoUP9QzF1io').worksheet('Наявність')
	for record in veh_list:
		if record.status == 0:
			try:
				hplink = sheet1.find(record.veh_vin)
			except:
				break
				return HttpResponse('Not this time')
			hplink_dir = sheet1.acell('D%s'%str(hplink.row),'FORMULA').value
			hplink_dir = hplink_dir.replace('=HYPERLINK("','')
			veh_folder = hplink_dir = hplink_dir.replace('";"%s")'%record.veh_vin,'')
			to_update = Gdrive_vehicles.objects.filter(id=record.id).update(veh_folder=veh_folder, status=1)
			veh_folder = hplink = ''
	return HttpResponse("<h1>Photos has been grabbed successfully</h1>")
"""
