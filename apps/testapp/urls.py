from django.urls import path, include
from . import views

urlpatterns = [
	path('grab_vehs', views.grab_vehs, name='grab_vehs'),
	path('grab_photos', views.grab_photos, name='grab_photos'),
]
