#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
import smtplib
from email.mime.text import MIMEText
from email.header    import Header

def index(request):
	return render(request, 'greenhub_auction/base_greenhub_auction.html');

def smtplib_login():
	server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
	server.login("elon.electrocars@gmail.com", "qoqbtqeyymrnuhtr")
	return server

def client(request):
	server = smtplib_login();
	recipients = ['bobenser@gmail.com']
	inner_msg = 'Тел: %s,\r\nТип кузова: %s,\r\n Тип топлива: %s,\r\n %s - %s ,\r\n Бюджет: %s,\r\n Комментарий: %s'%(
			  	request.POST.get('phone'),
			  	request.POST.get('veh_type'),
			  	request.POST.get('veh_fuel'),
			  	request.POST.get('veh_year1'),
			  	request.POST.get('veh_year2'),
			  	request.POST.get('veh_budget'),
			  	request.POST.get('message'))
	msg = MIMEText(inner_msg, 'plain', 'utf-8')
	msg['Subject'] = Header('Клиент на Аукцион', 'utf-8')
	msg['From'] = 'greenhub@greenhub.pro'
	# msg['To'] = ", ".join(recipients)

	server.sendmail(
	  	msg['From'],
	  	recipients,
		msg.as_string())
	server.quit()
	return HttpResponse(True)
