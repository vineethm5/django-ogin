from django.shortcuts import render

# Create your views here.
def singup(req):
    return render(req,"register.html")

def login(req):
    return render(req,"login.html")