from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.index, name='greenhub_auction'),
	path('client', views.client, name="aux_client"),
]
