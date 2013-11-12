from django.db import models

class Project(models.Model):


	title = models.CharField(max_length=250,verbose_name='Project Title')
	description = models.CharField(max_length=2500,verbose_name='Project Description')
	time =models.FloatField(verbose_name='Project Estimated Time')
	when = models.DateTimeField(auto_now_add=True,verbose_name='Project Created On')
