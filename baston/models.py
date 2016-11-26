from django.db import models

# Create your models here.

class Baston(models.Model):
	fecha = models.DateField(auto_now_add=True)
	comentario = models.CharField(max_length = 50,null=False, default='')

	def __str__(self):
		return self.comentario
