from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from blog.models import Blog
from django.contrib import messages

# Create your views here.


def blogHome(request):
    if request.user.is_authenticated:
        allBlogs = Blog.objects.all().order_by('-timeStamp')
        context = {'allBlogs': allBlogs}
        return render(request, 'blog/blogHome.html', context)
    else:
        return HttpResponseRedirect('/signin')

def blogDashboard(request):
    if request.user.is_authenticated:
        allBlogs = Blog.objects.all().filter(author=request.user).order_by('-timeStamp')
        context = {'allBlogs': allBlogs}
        return render(request, 'blog/dashboard.html', context)
    else:
        return HttpResponseRedirect('/signin')

def deleteBlog(request, slug):
    if request.user.is_authenticated:
        blog = Blog.objects.all().filter(author=request.user).filter(sno=slug)
        item = blog.get(sno=slug)
        blog.delete()
        messages.success(request, "Your blog entitled "+ item.title + " has been deleted")
        return HttpResponseRedirect('/blog/dashboard')
    else:
        return HttpResponseRedirect('/signin')


def blogPost(request, slug):
    blog = Blog.objects.filter(sno=slug).first()
    context = {'blog': blog}
    return render(request, 'blog/blogPost.html', context)
    # return HttpResponse(f"Blog Post: {slug}")


def blogCreate(request):
    if request.method == "POST":
        url = request.POST['url']
        title = request.POST['title']
        content = request.POST['content']
        author = request.user
        if(len(url) < 1 or len(title) < 1 or len(content) < 1):
            messages.error(request, "Please fill all the input fields")
        else:
            blog = Blog(title=title, content=content,
                        author=author, urlToImage=url)
            blog.save()
            messages.success(
                request, "Your blog has been created successfully")
    return render(request, 'blog/blogCreate.html')
