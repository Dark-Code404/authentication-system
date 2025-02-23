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

    def save(self, commit=True, user=None):
        """
        Save the Todo item, associating it with a user if provided.
        """
        instance = super().save(commit=False)
        if user is not None:
            instance.user = user

            if commit:
                instance.save()

            return instance


class Update_TodoForm(forms.ModelForm):
    """
    Form for updating an existing Todo item.
    Includes fields for name, description, completion date, and completion status.
    """
    class Meta:
        model = Todo
        fields = ["name", "description", "complete_date", "is_complete"]

    def save(self, commit=True, user=None):
        """
        Save the updated Todo item, associating it with a user if provided,
        and updating the completion status if specified.
        """
        instance = super().save(commit=False)
        if user is not None:
            instance.user = user

            if self.cleaned_data.get("is_complete"):
                instance.is_complete = True

            if commit:
                instance.save()

            return instance
