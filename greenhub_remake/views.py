from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail

def index(request):
	return render(request, 'index.html')

def contacts(request):
	return render(request, 'contacts.html')

def charger_map(request):
	return render(request, 'charger_map.html')
