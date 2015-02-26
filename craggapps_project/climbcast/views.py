from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Test setup for CraggApps\ClimbCast <br/><a href='/climbcast/about/'>About ClimbCast</a>")

def about(request):
    return HttpResponse("This is the default about view for CraggApps\ClimbCast")
