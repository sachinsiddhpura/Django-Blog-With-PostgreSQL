from django.db import models

# Create your models here.
from django.utils import timezone

class Blog(models.Model):
	title	=models.CharField(max_length=140)
	body	=models.TextField()
	created	=models.DateField(default=timezone.now().strftime("%Y-%m-%d"))

	class Meta:
		verbose_name	='Post'
		verbose_name_plural	="Posts"

	def __str__(self):
		return self.title