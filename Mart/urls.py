from django.contrib import admin
from django.urls import path,include
from Mart import views

urlpatterns = [
	path('',views.index,name='index page'),
	path('login',views.login,name='index page'),
	path('signup',views.signup,name='signup page'),
	path('signin',views.signin,name='signin page'),
	path('logout',views.logout,name='index page'),
]