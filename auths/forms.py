from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CusUser, Todo


class UserRegisterForm(UserCreationForm):
    """
    Form for user registration, including fields for username, email, password, and role.
    It inherits from Django's UserCreationForm and uses the CusUser model.
    """
    class Meta:
        model = CusUser
        fields = ["username", "email", "password1", "password2", "role"]


class UserLoginForm(forms.Form):
    """
    Form for user login, requiring a username and password.
    Utilizes standard form fields with custom CSS classes for styling.
    """
    username = forms.CharField(
        label="Username",
        max_length=150,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    password = forms.CharField(
        label="Password", widget=forms.PasswordInput(attrs={"class": "form-control"})
    )


class TodoForm(forms.ModelForm):
    """
    Form for creating or updating a Todo item.
    Includes fields for name, description, and completion date.
    Allows setting the user associated with the Todo.
    """
    class Meta:
        model = Todo
        fields = ["name", "description", "complete_date"]
        widgets = {
            'complete_date': forms.DateInput(attrs={'type': 'date'})

        }


class Update_TodoForm(forms.ModelForm):
    """
    Form for updating an existing Todo item.
    Includes fields for name, description, completion date, and completion status.
    """
    class Meta:
        model = Todo
        fields = ["name", "description", "complete_date", "is_complete"]

        widgets = {
            'complete_date': forms.DateInput(attrs={'id': 'datepicker', 'type': 'date'})

        }
