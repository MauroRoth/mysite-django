from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def indexName(request, name):
    return HttpResponse("Hello "+ name.upper())

def index(request):
    return HttpResponse("Hello World!!!")

