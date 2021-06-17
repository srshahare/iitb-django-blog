from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home/home.html')
    # return HttpResponse("Blog Home")

def contact(request):
    return HttpResponse("contact")

def about(request):
    return HttpResponse("about")
