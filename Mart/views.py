from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,auth


# Create your views here.
def index(request):
	return render(request,"index.html")

def signup(request):
	return render(request,"signup.html")

def signin(request):
	return render(request,"signin.html")

def logout(request):
	return redirect(request,"index.html")

def login(request):
	return render(request,"login.html")