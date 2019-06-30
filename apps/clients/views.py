#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
import smtplib
from email.mime.text import MIMEText
from email.header    import Header
from .models import Clients

def smtplib_login():
	server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
	server.login("elon.electrocars@gmail.com", "qoqbtqeyymrnuhtr")
	return server

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

	server = smtplib_login();
	recipients = ['greenhub.ua@gmail.com',]
	inner_msg = 'Имя: %s. \r\nТел: %s'%(request.POST.get('name'), request.POST.get('phone'))
	msg = MIMEText(inner_msg, 'plain', 'utf-8')
	msg['Subject'] = Header('Тест Драйв', 'utf-8')
	msg['From'] = 'greenhub@greenhub.pro'
	try:
		server.sendmail(
	  		msg['From'],
		  	recipients,
			msg.as_string())
	except:
		print("We've got a situation here")
		with open('/home/greenhub/django/logs/smtp.log', 'at', encoding='utf-8') as File:
			File.write('Error \n');
			File.close();
	finally:
		server.quit()
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

	server = smtplib_login();
	recipients = ['greenhub.ua@gmail.com',]
	inner_msg = 'Имя: %s. \r\nТел: %s'%(request.POST.get('name'), request.POST.get('phone'))
	msg = MIMEText(inner_msg, 'plain', 'utf-8')
	msg['Subject'] = Header('Перезвонить', 'utf-8')
	msg['From'] = 'greenhub@greenhub.pro'
	server.sendmail(
	  	msg['From'],
	  	recipients,
		msg.as_string())
	server.quit()
	return HttpResponse(True)
