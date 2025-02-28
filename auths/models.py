from django.db import models
from django.contrib.auth.models import AbstractUser


Choices = {
    ('USER_ROLE_ADMIN', "Admin user"),
    ('USER_ROLE_REGULAR', "Regular user"),
}


class CusUser(AbstractUser):
    """Custom user model with an additional 'role' field (Admin or Regular)."""
    role = models.CharField(max_length=100, choices=Choices, default="USER_ROLE_ADMIN")


class Todo(models.Model):
    user = models.ForeignKey(
        CusUser, related_name="user_post", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)
    description = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    complete_date = models.DateField(blank=True, null=True)
    is_complete = models.BooleanField(default=False)

    class Meta:
        ordering = ["-date_posted"]

    def __str__(self):
        return self.name
