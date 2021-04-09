from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib import messages
from register.forms import UserForm
from django.contrib.auth.models import User, auth
import json
def User_View(request):
    context ={}
    if request.POST:
        form = UserForm(request.POST)
        
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            name = form.cleaned_data.get('firstname')
            raw_password = form.cleaned_data.get('password1')
            UserRegister = authenticate(request, username =username, password = raw_password)
            
            login(request, UserRegister)
           
            return redirect('userhomepage')
        else:
            context['registration_form'] = form
    else:
        form = UserForm()
        context['registration_form'] = form
    return render(request,'register/register.html', context)


def user_login(request):
    context ={}
    if request.method == "POST":
       
        username= request.POST["username"]
        password = request.POST["password"]
        
        
        user = authenticate( username = username,password =password)
        
        if user is not None:
            print("++++++++++")
            login(request, user)
            return redirect('userhomepage')
        else:
            print("-------")
            messages.error(request, "invalid credentials")
            return render(request, "register/login.html")
    else:
        messages.error(request, "invalid credentials")
        return render(request, "register/login.html")
def logout(request):
    auth.logout(request)
    return render(request,"register/login.html")