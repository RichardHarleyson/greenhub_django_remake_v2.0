from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from .models import Gdrive_vehicles
# Googledrive modules
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from oauth2client import file, client, tools
from apiclient.discovery import build
from httplib2 import Http


credentials_path = 'C://Python64//greenhub_pydrive//credentials.json'
client_secret_path = 'C://Python64//greenhub_pydrive//client_secret.json'
client_json_path = 'C://Python64//greenhub_pydrive//client_secret_.json'

def grab_vehs(request):
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
	sheet_records = sheet1.get_all_records()
	for record in sheet_records:
		if str(record['Марка авто']) == '':
			continue
		vehicle = dict()
		if(str(record['Марка авто'])) == '':
			break
		if(str(record['Бронювання']) != '' and str(record['Бронювання']) != 'Акція'):
			continue
		vehicle['veh_title'] = '{} {} {}'.format(str(record['Марка авто']), str(record['Комплектація']), str(record['Мод рік']))
		vehicle['veh_vin'] = str(record['VIN'])
		# Получаем ссылку на ресурс с фото
		hplink = sheet1.find(record['VIN'])
		# hplink_dir = sheet1.acell('D%s'%str(hplink.row),'FORMULA').value
		# if 'google' in hplink_dir:
		# 	if 'folders' in hplink_dir:
		# 	   hplink_dir = hplink_dir.replace('=HYPERLINK("https://drive.google.com/drive/folders/','')
		# 	else:
		# 	   hplink_dir = hplink_dir.replace('=HYPERLINK("https://drive.google.com/open?id=',"")
		# 	   hplink_dir = hplink_dir.replace('";"%s")'%record['VIN'],'')
		# else:
		# hplink_dir = hplink_dir.replace('=HYPERLINK("','')
		# vehicle['veh_dir'] = hplink_dir.replace('";"%s")'%record['VIN'],'')
		print(vehicle)
		new_vehicle = Gdrive_vehicles(
			veh_title = vehicle['veh_title'],
			veh_vin = vehicle['veh_vin'])
		try:
			new_vehicle.save()
		except:
			continue
		del(vehicle)
	return HttpResponse("Seems we're okay")

def grab_photos(request):
	veh_list = Gdrive_vehicles.objects.all()
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
			print(veh_folder)
			# record.veh_folder = str(veh_folder)
			# record.status = 1
			# record.save()
			to_update = Gdrive_vehicles.objects.filter(id=record.id).update(veh_folder=veh_folder, status=1)
			veh_folder = hplink = ''
	return HttpResponse("Seems we're fine")
