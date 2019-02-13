from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail

def index(request):
	content = {'header' : 'Question', 'lable1' : 'This is a form', 'btn_text' : 'Button?', 'id' : 3}
	return render(request, 'testapp/base_testapp.html', context={'content' : content})

def testapp_method(request):
	# idata = request.GET['name']
	# print(idata)
	send_mail(
	'Тут такое дело...',
	'В общем, %s просит перезвонить по номеру %s'%(request.GET['name'], request.GET['phone']),
	'greenhub@greenhub.pro',
	['richard.harleyson@gmail.com'],
	fail_silently=False,
	)
	return HttpResponse(True)
