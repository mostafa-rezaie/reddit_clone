from django.shortcuts import render
from rest_framework import generics
from .models import Post
from .serializer import PostSerializer
# Create your views here.

class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
