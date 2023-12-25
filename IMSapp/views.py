from django.shortcuts import render
from django.http import HttpResponse
from .models import Items

# Create your views here.
def home(request):
    return HttpResponse("You are in home")

def stockin(request):
    pass

def stockout(request):
    pass
