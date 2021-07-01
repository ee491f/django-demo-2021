from django.db import models

# Create your models here.

class Greeting(models.Model):
    message = models.CharField(max_length=200)
    related_greeting = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True)

