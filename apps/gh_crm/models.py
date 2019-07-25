from django.db import models

class Crm_Clients(models.Model):
	client_name = models.CharField(max_length=70, default='empty', null=True)
	client_type = models.CharField(max_length=50, default='empty', null=True)
	veh_body = models.CharField(max_length=250, default='empty', null=True)
	veh_fuel = models.CharField(max_length=30, default='empty', null=True)
	veh_year1 = models.CharField(max_length=10, default='empty', null=True)
	veh_year2 = models.CharField(max_length=10, default='empty', null=True)
	veh_budget = models.CharField(max_length=15, default='empty', null=True)
	client_phone = models.CharField(max_length=12, default='empty', null=True)
	client_email = models.CharField(max_length=50, default='empty', null=True)
	client_comment = models.CharField(max_length=500, default='empty', null=True)
	client_status = models.BooleanField()
	client_join_date = models.CharField(max_length=30, default='empty')
	trashed_date = models.CharField(max_length=30, default='empty')
	isvisible = models.BooleanField(default=True)

	def __str__(self):
		return self.client_name

class Crm_Events(models.Model):
	client_id = models.ForeignKey(Crm_Clients, on_delete=models.CASCADE, related_name="event_client")
	event_type = models.CharField(max_length=20, default='empty',)
	event_date = models.CharField(max_length=20, default='empty',)
	event_status = models.CharField(max_length=20, default='empty',)
	event_creator = models.CharField(max_length=20, default='empty')
	event_curator = models.CharField(max_length=20, default='empty')
	event_comment = models.CharField(max_length=500, default='empty',)
	event_state = models.BooleanField(default=True)
	isvisible = models.BooleanField(default=True)

class Client_file(models.Model):
	client_file = models.FileField(upload_to='clients/%Y/%m_%d/', blank=False)
	client_id = models.ForeignKey(Crm_Clients, on_delete=models.CASCADE, related_name='photos')
	photo_status = models.BooleanField(default=True)
