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
		# Проверяем доступно ли авто
		if str(record['Марка авто']) == '' or str(record['Статус']) != 'Готова' :
			continue
		if(str(record['Бронювання']) != '' and str(record['Бронювання']) != 'Акція'):
			continue
		# Словарь данных об авто
		vehicle = dict()
		vehicle['veh_title'] = '{} {} {}'.format(str(record['Марка авто']), str(record['Комплектація']), str(record['Мод рік']))
		vehicle['veh_comp'] = str(record['Комплектація'])
		vehicle['veh_vin'] = str(record['VIN'])
		vehicle['veh_year'] = str(record['Мод рік'])
		vehicle['veh_mileage'] = str(record[''])
		vehicle['veh_color_in'] = str(record[''])
		vehicle['veh_color'] = str(record[''])
		vehicle['veh_price'] = str(record[''])
		vehicle['veh_photo'] = str(record[''])
		vehicle['veh_battery'] = str(record[''])
		vehicle['veh_info'] = ''
		vehicle['veh_type'] = 'dealler'
		vehicle['veh_status'] = 0
		# Получаем ссылку на ресурс с фото
		vehicle['veh_folder'] = str(record[''])
		hplink = sheet1.find(record['VIN'])
		new_vehicle = Gdrive_vehicles(
			veh_title = vehicle['veh_title'],
			veh_vin = vehicle['veh_vin'])
		try:
			new_vehicle.save()
		except:
			continue


		del(vehicle)
	return HttpResponse("<h1>Vehicles has been grabbed successfully</h1>")

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
			to_update = Gdrive_vehicles.objects.filter(id=record.id).update(veh_folder=veh_folder, status=1)
			veh_folder = hplink = ''
	return HttpResponse("<h1>Photos has been grabbed successfully</h1>")
