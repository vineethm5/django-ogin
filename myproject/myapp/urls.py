from django.urls import path
from .views import *

urlpatterns=[
   path("",singup,name='index'),
]