from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .forms import Signup,Login
from django.core.mail import send_mail, BadHeaderError
from .models import UserInfo
# Create your views here.
def index(request):
	return render(request,"index.html")

def signup(request):
	if request.method == "POST":
		form = Signup(request.POST)
		if form.is_valid():
			firstName = form.cleaned_data["first_name"]
			lastName = form.cleaned_data["last_name"]
			email = form.cleaned_data["email_address"]
			phone = form.cleaned_data["phone"]
			password = form.cleaned_data["password"]
			username = "".join([firstName,lastName])
			if User.objects.filter(username=username).exists():
				form = Signup()	
				return render(request,"signup.html",{"form":form})
			else:
				User.objects.create_user(username=username,password=password,first_name=firstName,last_name=lastName,email=email).save()
				UserInfo(firstName=firstName,lastName=lastName,email=email,phone=phone,password=password,).save()
				return redirect("/login")
	form = Signup()	
	return render(request,"signup.html",{"form":form})

@login_required(login_url='login')
def main(request):
	return render(request,"main.html")

def logout(request):
		return redirect(request,"index.html",{"from":form})

def login(request):
	if request.method == "POST":
		form = Login(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = auth.authenticate(username=username,password=password)
			if user is not None:
				auth.login(request,user)
				return redirect("./main")
			else:
				messages.success(request,("Enter the correct username and password !"))
				return redirect("./login",{"form":form})
	else:
		form = Login()
		return render(request,"login.html",{"form":form})