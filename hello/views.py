from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def greet (request, name):
    return render(request,'hello/greet.html',{
        "name": name.capitalize(),
    })

def index(request):
    return render(request, 'hello/index.html')

# def greet(request, name):
#     return HttpResponse(f"<h2>Hello {name.capitalize()}!!!</h2>")

# def index(request):
#     return HttpResponse("Hello World!!!")

