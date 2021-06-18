from django.contrib import messages
from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from newsapi import NewsApiClient
import json

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        newsapi = NewsApiClient(api_key='eb76b7f40b8c4633b1b123f7bff7dc12')
        top_headlines = newsapi.get_top_headlines()
        articles = top_headlines['articles']
        context = {'articles': articles}
        return render(request, 'home/home.html', context)
    else:
        return HttpResponseRedirect('/signin')

def handleLogout(request):
    logout(request)
    return HttpResponseRedirect('/signin')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            messages.error(request, "Invalid Credentials, Please try again")
    return render(request, 'home/signin.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']    
        email = request.POST['email']    
        pass1 = request.POST['password']    
        pass2 = request.POST['confirm_password']    

        #check for error in inputs
        #passwourd should match
        if(pass1 != pass2):
            messages.error(request, "Please check your form details, Password mismatched!")
        
        #username should containe alphanum char
        if not username.isalnum():
            messages.error(request, "Please check your form details, Username should only contain alphanumeric characters!")

        #after passing all checks trigger this block
        else:
             #if username exist in the db
            try:
                user = User.objects.get(username = username)
                messages.error(request, "Username is already exist, Try to login instead")
            except User.DoesNotExist:
                myuser = User.objects.create_user(username, email, pass1)
                myuser.save()
                return HttpResponseRedirect("/")
    return render(request, 'home/signup.html')