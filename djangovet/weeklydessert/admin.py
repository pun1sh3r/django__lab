from django.contrib import admin

# Register your models here.
from .models import Week, Choice
admin.site.register(Week)
admin.site.register(Choice)