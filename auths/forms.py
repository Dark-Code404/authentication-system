from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CusUser, Todo


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = CusUser
        fields = ["username", "email", "password1", "password2", "role"]


class UserLoginForm(forms.Form):
    username = forms.CharField(
        label="Username",
        max_length=150,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    password = forms.CharField(
        label="Password", widget=forms.PasswordInput(
            attrs={"class": "form-control"})
    )


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ["name", "description", "complete_date"]

    def save(self, commit=True, user=None):

        instance = super().save(commit=False)
        if user is not None:
            instance.user = user

            if commit:
                instance.save()

            return instance


class Update_TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ["name", "description", "complete_date", "is_complete"]

    def save(self, commit=True, user=None):

        instance = super().save(commit=False)
        if user is not None:
            instance.user = user

            if self.cleaned_data.get("is_complete"):
                instance.is_complete = True

            if commit:
                instance.save()

            return instance
