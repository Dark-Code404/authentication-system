from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .forms import UserRegisterForm, UserLoginForm, TodoForm, Update_TodoForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .models import CusUser, Todo


@login_required()
def home(request: HttpRequest) -> HttpResponse:
    """
    Displays the home page with all Todo items.
    Requires the user to be logged in.
    """
    todos = Todo.objects.all()
    context = {"todos": todos}
    return render(request, "home.html", context)


def register(request: HttpRequest) -> HttpRequest:
    """
    Handles user registration by creating a new user account.
    Displays an error message if the username already exists.
    """
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            if CusUser.objects.filter(username=username).exists():
                messages.info(request, "user already exist")
                return render(request, "auth/register.html", {"form": form})

            form.save()
            messages.success(request, "account created")
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, "auth/register.html", {"form": form})


def user_login(request: HttpRequest) -> HttpResponse:
    """
    Authenticates the user and logs them in.
    Displays an error message for invalid credentials or non-admin users.
    """
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = CusUser.objects.filter(username=username).first()

            if user is None:
                messages.info(request, "user doesnot exist")
            elif user.role != "USER_ROLE_ADMIN":
                messages.info(request, f"{username} is not a Admin user")
            else:
                user = authenticate(request, username=username, password=password)
                if user:
                    login(request, user)
                    return redirect("home")
                else:
                    messages.error(request, "You have entered invalid password")
    else:
        form = UserLoginForm()
    return render(request, "auth/login.html", {"form": form})


def create_todo(request: HttpRequest) -> HttpResponse:
    """
    Handles the creation of a new Todo item.
    Saves the Todo item with the logged-in user and redirects to the home page.
    """
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.user = request.user
            user.save()

            return redirect("home")
    else:
        form = TodoForm()
    return render(request, "Todo/create_todo.html", {"form": form})


def update_todo(request: HttpRequest, pk: int = None) -> HttpResponse:
    """
    Allows the user to update a Todo item.
    Checks for ownership of the Todo and redirects to home on success.
    """
    task = get_object_or_404(Todo, id=pk)
    if request.method == "POST":
        form = Update_TodoForm(request.POST, instance=task)
        if request.user == task.user:
            if form.is_valid():
                is_complete = form.cleaned_data.get('is_complete')
                user_todo = form.save(commit=False)
                user_todo.is_complete = is_complete
                user_todo.save()
                return redirect("home")
        else:
            messages.error(request, "You are not authorized user")
    else:
        form = Update_TodoForm(instance=task)
    return render(request, "Todo/update_todo.html", {"form": form})


def delete_todo(request: HttpRequest, pk: int = None) -> HttpResponse:
    """
    Allows the user to delete a Todo item.
    Ensures the user is the owner of the Todo before deletion.
    """
    task = get_object_or_404(Todo, id=pk)
    if request.method == "POST":
        if request.user == task.user:
            task.delete()
            return redirect("home")
        else:
            messages.error(request, "You are not authorized user")
    return render(request, "Todo/delete_todo.html", {"task": task})
