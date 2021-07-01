from django.contrib import admin
from .models import Greeting, GreetingPair

# Register your models here.
admin.site.register([
  Greeting,
  GreetingPair,
])
