from django import forms
from .models import UserInfo

class Signup(forms.Form):
	first_name = forms.CharField(max_length = 50,widget=forms.TextInput(attrs={'class':"form-control","placeholder":"Enter first name"}))
	last_name = forms.CharField(max_length = 50,widget=forms.TextInput(attrs={'class':"form-control","placeholder":"Enter last name"}))
	email_address = forms.EmailField(max_length = 254,widget=forms.EmailInput(attrs={'class':"form-control","placeholder":"Enter Email"}))
	phone = forms.IntegerField(widget=forms. NumberInput(attrs={'class':"form-container","placeholder":"Enter phone"}))
	password = forms.CharField(max_length = 50,widget=forms.PasswordInput(attrs={'class':"form-control","placeholder":"Enter Password"}))

class Login(forms.Form):
	username = forms.CharField(max_length = 100,widget=forms.TextInput(attrs={'class':"form-control","placeholder":"Enter first name"}))
	password = forms.CharField(max_length = 50,widget=forms.TextInput(attrs={'class':"form-control","placeholder":"Enter Password"}))

# class Signup(forms.ModelForm):
#     class Meta:
#         model = UserInfo
#         fields= ("firstName","lastName","email","phone","password")

#         widgets ={
#         	"firs tName":forms.TextInput(attrs={'class':"form-control","placeholder":"Enter first name"}),
#         	"last Name":forms.TextInput(attrs={'class':"form-control","placeholder":"Enter first name"}),
#         	"email":forms.TextInput(attrs={'class':"form-control","placeholder":"Enter first name"}),
#         	"phone":forms.TextInput(attrs={'class':"form-control","placeholder":"Enter first name"}),
#         	"password":forms.TextInput(attrs={'class':"form-control","placeholder":"Enter first name"})
#         }