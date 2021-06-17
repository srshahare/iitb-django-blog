from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def blogHome(request):
    return render(request, 'blog/blogHome.html')
    # return HttpResponse("Blog Home")

def blogPost(request, slug):
    return render(request, 'blog/blogPost.html')
    # return HttpResponse(f"Blog Post: {slug}")
