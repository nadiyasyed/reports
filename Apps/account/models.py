from django.db import models
from django.contrib.auth.models import User
from account.utils import ROLE_CHOICES


class CustomUser(User):


	role = models.CharField(max_length = 32,choices = ROLE_CHOICES)
	date_created = models.DateTimeField(auto_now_add = True)
	last_modified = models.DateTimeField(auto_now = True)

class Employe(models.Model):
	name =  models.CharField(max_length = 32)
	addr =  models.CharField(max_length = 32)
	
	


