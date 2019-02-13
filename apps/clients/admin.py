from django.contrib import admin
from .models import Clients

class MainAdmin(admin.ModelAdmin):
	list_display = ('client_name', 'client_phone', 'client_stage', 'client_status', 'client_join_date')
	search_fields = ('client_name', 'client_phone')

admin.site.register(Clients, MainAdmin)
