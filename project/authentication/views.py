from django.shortcuts import render
from . import models

def home(request):
    return HttpResponse("Hello world")
