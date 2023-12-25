from django.shortcuts import render
from django.http import HttpResponse
from .models import Items

# Create your views here.
def home(request):
    return HttpResponse("You are in home")

def stockin(request):
    item = Items.objects.get()

def stockout(request):
    pass
