from django.db import models

class Clients(models.Model):
	client_name = models.CharField(max_length=50, null=True, blank=True)
	client_phone = models.CharField(max_length=20, unique=True)
	client_stage = models.CharField(max_length=20, null=True, blank=True)
	client_status = models.BooleanField()
	client_join_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.client_name
