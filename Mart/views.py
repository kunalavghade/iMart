from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .forms import Signup,Login,ContactUsForm
from django.core.mail import send_mail, BadHeaderError
from .models import UserInfo,ContactUs
from django.http import JsonResponse
from json import dumps
import requests

compony = {
	"TCS":"TCS",
	"Wipro":"WTI",
	"ICIC Bank":"IBN",
	"Tata Motors":"TTM",
	"Infosys":"INFY",
	"SBI":"SBI",
	"Tesla":"TSLA",
	"Amazon":"AMZN",
	"Google":"GOOGL",
	"IBM":"IBM"
	}

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

@login_required(login_url='/login')
def main(request):
	if request.method == "POST":
		comp = request.POST['company']
		print(comp)
	else:
		comp = "Google"
	time = []
	value = []
	url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={compony[comp]}&apikey=9GI559N6X7ZBUR94'
	r = requests.get(url)
	data = r.json()
	count = 0
	for i in data["Time Series (Daily)"]:
		time.append(i)
		value.append(float(data["Time Series (Daily)"][i]["2. high"]))
		count+=1
		if(count == 30):
			break
	maxval = max(value)
	minval = min(value)
	open_val = round(float(data["Time Series (Daily)"][time[0]][ "1. open"]),2)
	close_val = round(float(data["Time Series (Daily)"][time[0]]["4. close"]),2)
	volume_val = round(float(data["Time Series (Daily)"][time[0]]["5. volume"]),2)
	last_open = round(float(data["Time Series (Daily)"][time[1]][ "1. open"]),2)
	response = requests.get('https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=f3831cf4b9e34369843e9062f75e80f1')
	news = response.json()
	news_title = []
	news_disc = []
	for i in range(6):
		news_title.append(news["articles"][i]["title"])

	data = {
		"time":time[::-1],
		"value":value[::-1],
		"max":maxval,
		"min":minval,
		"open":open_val,
		"close":close_val,
		"volume":volume_val,
		"last_open":last_open,
		"news_title": news_title, 
		}
		
	stock = {
		"title":comp,
		"open":open_val,
		"close":close_val,
		"volume":volume_val,
		"last_open":last_open
	}
	data=dumps(data)
	return render(request,"main.html",{'data': data,"stock":stock})

def logout(request):
	auth.logout(request)
	return redirect("./login")

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

def about(request):
	return render(request,"about.html")

def contactus(request):
	if request.method == "POST":
		form = ContactUsForm(request.POST)
		if form.is_valid():
			your_name = form.cleaned_data["your_name"]
			email_address = form.cleaned_data["email_address"]
			Your_message = form.cleaned_data["Your_message"]
			ContactUs(Your_message=Your_message,email_address=email_address,your_name=your_name).save()
			return redirect("/login")
	else:
		form = ContactUsForm()
		return render(request,"contactus.html",{"form":form})