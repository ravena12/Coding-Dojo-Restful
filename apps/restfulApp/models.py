from __future__ import unicode_literals
from django.db import models
from django.contrib  import messages



class Products(models.Model):
	name = models.CharField(max_length = 255)
	description = models.CharField(max_length = 1000)
	price = models.CharField(max_length = 10)


