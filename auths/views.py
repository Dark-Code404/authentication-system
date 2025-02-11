from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm,UserLoginForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,authenticate
from .models import CusUser
 

 
@login_required()
def home(request):

    
    return render(request,"auth/home.html")


def register(request):
    
    if request.method=="POST":
        form=UserRegisterForm(request.POST)

        if form.is_valid():
            username=form.cleaned_data.get("username")
            if CusUser.objects.filter(username=username).exists():
                messages.info("user already exist")
            
            form.save()
            messages.success(request,f"account created for {username}.")
            return redirect('login')

    else:
         
        form=UserRegisterForm()
    return render(request,"auth/register.html",{"form":form})


 


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            
            user = CusUser.objects.filter(username=username).first()

            if user is  None:
                messages.info(request,"user doesnot exist")
            elif user.role!='role1':
                messages.info(request,f"{username} is not a Admin user")

            else:
                user=authenticate(request,username=username,password=password)
                if user:

                    login(request, user)  
                    return redirect('home')  
                else:
                 
                    messages.error(request, 'You have entered invalid   password')
    else:
        form = UserLoginForm()
    return render(request, 'auth/login.html', {'form': form})

