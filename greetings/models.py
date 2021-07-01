from django.db import models

# Create your models here.

class Greeting(models.Model):
    message = models.CharField(max_length=200)
    related_greetings = models.ManyToManyField('self', through="GreetingPair")

class GreetingPair(models.Model):
    initial_greeting = models.ForeignKey(Greeting, on_delete=models.SET_NULL, related_name="initial_greeting", blank=True, null=True)
    responding_greeting = models.ForeignKey(Greeting, on_delete=models.SET_NULL, related_name="responding_greeting", blank=True, null=True)
    comment = models.CharField(max_length=200)
