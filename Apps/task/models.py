from django.db import models
from project.models import Project

class Task(models.Model):


	project = models.ForeignKey(Project,verbose_name='Project Title')
	title = models.CharField(max_length=250,verbose_name='Task Title')
	time =models.FloatField(verbose_name='Task Estimated Time')
	when = models.DateTimeField(auto_now_add=True,verbose_name='Task Created On')

