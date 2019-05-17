from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	
	return render(request, 'greenhub_auction/base_greenhub_auction.html');
