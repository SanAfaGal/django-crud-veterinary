from django.contrib import admin

from .models import Customer, Pet

admin.site.register(Customer)
admin.site.register(Pet)