from django.db import models

class Lead(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True) #each email must be unique
    message= models.CharField(max_length=500, blank=True) #makes adding a message optional
    created_at = models.DateTimeField(auto_now_add=True) #it adds the date automatically
