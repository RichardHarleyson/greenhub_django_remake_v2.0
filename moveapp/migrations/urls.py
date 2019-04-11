from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
	# Admin
    path('admin/', admin.site.urls),
	# Core pages
	path('', views.index, name='index'),
]
