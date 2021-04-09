from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def user_homepage(request):
    return render(request, "userhomepage/userhomepage.html")

