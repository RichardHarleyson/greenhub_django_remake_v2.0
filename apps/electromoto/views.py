from django.shortcuts import render

def index(request):
	return render(request, 'electromoto/base_electromoto.html')
