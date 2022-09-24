from wsgiref.util import request_uri
from django.shortcuts import render
from django.shortcuts import render, redirect
from datetime import*  
from django.http import HttpResponse
from base.models import Service

def home(request):
    serviceData = Service.objects.all()
    
    data = {'serviceData':
    serviceData}
    return render(request, "home.html",data)
  
def projects(request):
    return render(request, "projects.html")
  
def contact(request):
    return render(request, "contact.html")


def getcookie(request):
    show = request.COOKIES['home']
    html = "<center> New Page <br>{0}</center>".format(show)
    return HttpResponse(html)      




def setcookie(request):
    html = HttpResponse("<h1>Welcome to webpage</h1>")
    html.set_cookie('Page', 'We are setting a cookie for best experience ', max_age = None)
    return html    

def showcookie(request):
    show = request.COOKIES['Page']
    html = "<center> New Page <br>{0}</center>".format(show)
    return HttpResponse(html)   

def updating_cookie(request):
    html = HttpResponse("We are updating  the cookie which is set before")
    html.set_cookie('Page','Updated Successfully')
    return html