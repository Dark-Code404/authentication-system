from django.contrib import admin
from .models import Todo, CusUser

# Register your models here.
admin.site.register(CusUser)
admin.site.register(Todo)
