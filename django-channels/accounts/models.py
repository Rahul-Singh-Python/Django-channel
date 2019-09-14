from django.db import models

# Create your models here.

class rahul(models.Model):
	name=models.CharField(max_length=25)
	email=models.EmailField(max_length=50)
	state=models.CharField(max_length=25)

	def __str__(self):
		return self.name