from django.contrib import admin
from .models import Todo, CustomUser

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Todo)
