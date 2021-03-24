from django.db import models
# Create your models here.


class Employees(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255, default='')
	designation = models.CharField(max_length=255, blank=True)

	def __str__(self):
		return self.user.first_name
