from django.contrib import admin
from django.urls import path,include
from Mart import views

urlpatterns = [
	path('',views.index,name='index page'),
	path('login',views.login,name='login page'),
	path('signup',views.signup,name='signup page'),
	path('main',views.main,name='main page'),
	path('logout',views.logout,name='logout page')
]