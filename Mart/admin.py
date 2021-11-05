from django.contrib import admin
from . models import UserInfo
# Register your models here.

class UserInfoAdmin(admin.ModelAdmin):
	list_display = ("firstName","lastName","email","phone","password")


admin.site.register(UserInfo,UserInfoAdmin)