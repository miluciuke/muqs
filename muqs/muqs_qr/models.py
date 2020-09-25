from django.db import models

class Riddle(models.Model):
	title = models.CharField(max_length=100, unique=True)
	body = models.TextField()
	answer = models.TextField()
	def __str__(self):
		return self.title