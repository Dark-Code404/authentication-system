

from django.shortcuts import get_object_or_404, redirect, render
from .forms import UserRegisterForm, UserLoginForm, TodoForm, Update_TodoForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .models import CusUser, Todo


@login_required()
def home(request):
    todos = Todo.objects.all()
    context = {"todos": todos}

    return render(request, "home.html", context)


def register(request):

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


def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = CusUser.objects.filter(username=username).first()

            if user is None:
                messages.info(request, "user doesnot exist")
            elif user.role != "role1":
                messages.info(request, f"{username} is not a Admin user")

            else:
                user = authenticate(request, username=username,
                                    password=password)
                if user:

                    login(request, user)
                    return redirect("home")
                else:

                    messages.error(request,
                                   "You have entered invalid password")
    else:
        form = UserLoginForm()
    return render(request, "auth/login.html", {"form": form})


def create_todo(request):
    if request.method == "POST":

        form = TodoForm(request.POST)

        if form.is_valid():
            form.save(user=request.user)
            return redirect("home")

    else:

        form = TodoForm()
    return render(request, "Todo/create_todo.html", {"form": form})


def update_todo(request, pk):
    task = get_object_or_404(Todo, id=pk)
    if request.method == "POST":
        form = Update_TodoForm(request.POST, instance=task)
        if request.user == task.user:

            if form.is_valid():
                form.save(user=request.user)
                return redirect("home")

        else:
            messages.error(request, "You are not authorized user")

    else:

        form = Update_TodoForm(instance=task)
    return render(request, "Todo/update_todo.html", {"form": form})


def delete_todo(request, pk):

    task = get_object_or_404(Todo, id=pk)

    if request.method == "POST":
        if request.user == task.user:

            task.delete()
            return redirect("home")

        else:
            messages.error(request, "You are not authorized user")

    return render(request, "Todo/delete_todo.html", {"task": task})
