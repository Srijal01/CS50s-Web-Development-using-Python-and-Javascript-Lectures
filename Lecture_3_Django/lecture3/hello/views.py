from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "lecture3/hello/templates/hello/index.html")

def srijal(request):
    return HttpResponse("Hello, srijal!")

def greeet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })