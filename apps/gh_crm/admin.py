from django.contrib import admin
from .models import Crm_Clients, Crm_Events, Client_file

class MainAdmin(admin.ModelAdmin):
	list_display = (
		'id',
		'client_name',
		'client_phone',
		'client_email',
		'client_comment',
		'client_status',
		'isvisible',
		'trashed_date',
		'client_join_date'
		)

class MainAdmin2(admin.ModelAdmin):
	list_display = (
		'client_id',
		'event_type',
		'event_date',
		'event_status',
		'event_creator',
		'event_curator',
		'event_comment',
		'isvisible',
	)

class MainAdmin3(admin.ModelAdmin):
	list_display = (
		'id',
		'client_id',
		'client_file',
		'photo_status',
	)

admin.site.register(Crm_Clients, MainAdmin)
admin.site.register(Crm_Events, MainAdmin2)
admin.site.register(Client_file, MainAdmin3)
