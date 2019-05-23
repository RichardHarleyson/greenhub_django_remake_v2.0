"""greenhub_remake URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
import apps.clients.views as clients_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	# Admin
    path('admin/', admin.site.urls),
	# Core pages
	path('', views.index, name='index'),
	path('contacts/', views.contacts, name='contacts'),
	path('charger_map/', views.charger_map, name='charger_map'),
	path('policy/', views.policy, name="policy"),
	# Apps pages
	path('electrocars/', include('apps.electrocars.urls')),
	path('electromoto/', include('apps.electromoto.urls')),
	path('testapp/', include('apps.testapp.urls')),
	path('testdrive_form', clients_views.testdrive_form, name='testdrive_form'),
	path('callme_form', clients_views.callme_form, name='callme_form'),
	path('greenhub_auction/', include('apps.greenhub_auction.urls'), name='greenhub_auction')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
