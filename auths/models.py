from django.db import models

from django.contrib.auth.models import AbstractUser

Choices ={
    
"role1": "Admin user",
"role2": "Regular user",
}

class CusUser(AbstractUser):
    role=models.CharField(max_length=100,choices=Choices,default='role1')



