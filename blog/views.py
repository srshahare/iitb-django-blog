from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Blog Home")

def register(request):
    context = {}
    return render(request, 'blog/register.html', context)

def login(request):
    context = {}
    return render(request, 'blog/login.html', context)