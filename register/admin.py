from django.conf.urls import url
from .models import User, ExtractedRecipe
from django.contrib import admin
#from .models import Teacher_Register


##admin.site.register(Teacher_Register)
# Register your models here.
from django.contrib.auth.admin import UserAdmin
class User_admin(UserAdmin):
    list_display = ('first_name','last_name', 'username', 'email','contact_number', 'creation_date','modification_date')
    search_fields =('email', 'username')
    readonly_fields =('email',)
    filter_horizontal =()
    list_filter =() 
    fieldsets =()
admin.site.register(User, User_admin)
# class Recipe_Extracted(modelAdmin):
#     list_display = ('userId','recipe_template', 'recipe_url', 'creation_date','modification_date', 'source','recipe_title')
#     search_fields =('userId', 'recipe_template')
#     readonly_fields =('userId',)
#     filter_horizontal =()
#     list_filter =() 
#     fieldsets =()
admin.site.register(ExtractedRecipe)