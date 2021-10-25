from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,auth


# Create your views here.
def index(request):
	return HttpResponse("<H1> this is index </H1>")

def singup(request):
	pass

def singin(request):
	pass

def logout(request):
	pass

def login(request):
	pass