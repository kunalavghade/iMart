from django.db import models

class UserInfo(models.Model):
	firstName = models.CharField(max_length = 50)
	lastName = models.CharField(max_length = 50)
	email = models.EmailField(max_length = 254)
	phone = models.IntegerField()
	password = models.CharField(max_length = 50)

