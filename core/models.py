from django.db import models

# Create your models here.

class core(models.Model):
	SSN = models.IntegerField()
	lastname = models.TextField(max_length = 255)
	firstname = models.TextField(max_length = 255)
	birthday = models.DateField()
	phone = models.IntegerField(default=0)
	address = models.TextField()
	company = models.TextField()