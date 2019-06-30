from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.events_page, name='gh_crm_events_page'),
	path('clients_page', views.clients_page, name="gh_crm_clients_page"),
	path('add_client', views.add_client, name="gh_crm_add_client"),
	path('add_event', views.add_event, name="gh-crm_add_event"),
	path('update_event', views.update_event, name="gh_crm_update_event"),
	path('update_client', views.update_client, name="gh_crm_update_client"),
	path('remove_event', views.remove_event, name="gh_crm_remove_event"),
	path('remove_client', views.remove_client, name="gh_crm_remove_client"),
	path('update_event_status', views.update_event_status, name="gh_crm_update_event_status"),
	path('update_client_status', views.update_client_status, name="gh_crm_update_client_status"),

	path('event_page', views.event_page, name="gh_crm_event_page"),
]
