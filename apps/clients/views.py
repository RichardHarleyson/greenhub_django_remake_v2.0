from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from .models import Clients


def testdrive_form(request):
	try:
		# creating client in db
		new_client = Clients.objects.create(
			client_name=request.POST.get('name'),
			client_phone=request.POST.get('phone'),
			client_stage='new',
			client_status=True
			)
	except:
		return HttpResponse(False)
	print(new_client.id)
	print()
	send_mail(
	'Запись на тест драйв',
	'Имя: %s. Тел: %s'%(request.POST.get('name'), request.POST.get('phone')),
	'greenhub@greenhub.pro',
	['richard.harleyson@gmail.com'],
	fail_silently=False,
	)
	return HttpResponse(True)

def callme_form(request):
	try:
		# creating client in db
		new_client = Clients.objects.create(
			client_name=request.POST.get('name'),
			client_phone=request.POST.get('phone'),
			client_stage='new',
			client_status=True
			)
	except:
		return HttpResponse(False)

	send_mail(
	'Перезвонить',
	'Имя: %s. Тел: %s'%(request.POST.get('name'), request.POST.get('phone')),
	'greenhub@greenhub.pro',
	['richard.harleyson@gmail.com'],
	fail_silently=False,
	)
	return HttpResponse(True)
