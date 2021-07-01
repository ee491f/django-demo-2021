from django.db import models

# Create your models here.

class Farewell(models.Model):
    message = models.CharField(max_length=200)

class Greeting(models.Model):
    message = models.CharField(max_length=200)
    farewells = models.ManyToManyField(Farewell, through="SalutationValedictionPair")

class SalutationValedictionPair(models.Model):
    greeting = models.ForeignKey(Greeting, on_delete=models.CASCADE)
    farewell = models.ForeignKey(Farewell, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)

