from django.urls import path
from .views import *

urlpatterns=[
   path("",singup,name='index'),
   path("login/",login,name="login")
]