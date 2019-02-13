from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.index, name='testapp'),
	path('testapp_method', views.testapp_method, name='testapp_method')
]
