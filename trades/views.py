from django.http import HttpResponse
from tradewise.mongo_client import db
from django.shortcuts import render

def home(request):
    return render(request,"authentication/index.html")


def signup(request):
    return render(request,"authentication/signup.html")

def login(request):
    return render(request,"authentication/login.html")

def signout(request):
    pass