from django.urls  import path
from . import views
#from django.conf.urls import reverse
urlpatterns =[ 
path('', views.user_login, name  ='login'),
path('register', views.User_View, name ="register" ),]
