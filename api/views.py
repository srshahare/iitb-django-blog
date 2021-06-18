import json
from blog.models import Blog
from django.core import serializers
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class CreateApi(APIView):
    permission_classes = (IsAuthenticated, IsAdminUser)             # <-- And here
    def put(self, request):
        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            url = body['url']
            title = body['title']
            content = body['content']
            author = body['author']
            blog = Blog(title=title, content=content,
                            author=author, urlToImage=url)
            blog.save()
            content = {'status': 'Success', 
            'message': 'Blog created successfully'}
            return Response(content)
        except:
            content = {'status': 'Error', 
            'message': 'url, title, content, author should be there as a body'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)

class DeleteApi(APIView):
    permission_classes = (IsAuthenticated, IsAdminUser)             # <-- And here
    def delete(self, request):
        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            slug = body['slug']
            blog = Blog.objects.all().filter(sno=slug)
            blog.delete()
            content = {'status': 'Success', 
            'message': 'The blog is deleted'}
            return Response(content, status=status.HTTP_200_OK)
        except:
            content = {'status': 'Error', 
            'message': 'Error in deleting the blog'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)

class UpdateApi(APIView):
    permission_classes = (IsAuthenticated, IsAdminUser)             # <-- And here
    def post(self, request):
        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            slug = body['slug']
            blog = Blog.objects.get(sno=slug)

            url = body['url']
            title = body['title']
            content = body['content']
            author = body['author']

            blog.title = title
            blog.urlToImage = url
            blog.content = content
            blog.author = author

            blog.save()
            print(blog)
            content = {'status': 'Success', 
            'message': 'Blog updated successfully'}
            return Response(content)
        except:
            content = {'status': 'Error', 
            'message': 'slug, url, title, content, author should be there as a body'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)

class ListApi(APIView):
    permission_classes = (IsAuthenticated, IsAdminUser)             # <-- And here
    def get(self, request):
        blogs = Blog.objects.all()
        data = serializers.serialize("json", blogs)
        return Response(data)

class ViewApi(APIView):
    permission_classes = (IsAuthenticated, IsAdminUser)             # <-- And here
    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)
