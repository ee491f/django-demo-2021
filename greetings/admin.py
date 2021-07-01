from django.contrib import admin
from .models import Greeting, Farewell, SalutationValedictionPair

# Register your models here.
admin.site.register([
  Greeting,
  Farewell,
  SalutationValedictionPair,
])
