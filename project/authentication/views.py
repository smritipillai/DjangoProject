from django.shortcuts import render
from . import models
from django.http import HttpResponse

def Home(request):
    return HttpResponse("Hello world")
