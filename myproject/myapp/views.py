from django.shortcuts import redirect, render
from django.contrib.auth.models import  *
from django.contrib.auth import authenticate
from django.contrib import messages
from django.urls import reverse


# Create your views here.
def singup(req):
    if req.method == 'POST':
        username=req.POST.get("username")
        email=req.POST.get("email")
        password=req.POST.get("password")

        user=User.objects.filter(username=username)
        if user.exists():
            messages.info(req,"User already exits")
            return redirect("/")
        user=User.objects.create_user(
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save()
        messages.info(req,"Account created succesfully")
    return render(req,"register.html")

def login(req):
    if req.method == "POST":
        username=req.POST.get("username")
        password=req.POST.get("password")

        if not User.objects.filter(username=username).exists():
            messages.info(req,"Invalid UserName")
            return redirect("/login/")
        
        user=authenticate(username=username,password=password)
        if user is None:
            messages.info(req,"Invalid password")
        else:
            messages.info(req,"Login Successfull")
            return render(req,"home.html",context={"username":username})

    return render(req,"login.html")