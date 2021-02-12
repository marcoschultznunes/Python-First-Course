from django.shortcuts import render
from rest_framework import generics
from posts.models import Post, Tag
from posts.serializers import (
    PostDetailsSerializer, PostListSerializer, PostUpdateSerializer, 
    TagDetailsSerializer, TagListSerializer
)

# Post
class PostListView(generics.ListAPIView):
    queryset = Post.objects.all().order_by('title')
    serializer_class = PostListSerializer

class PostRetrieveView(generics.RetrieveAPIView):
    queryset = Post.objects.all().order_by('title')
    serializer_class = PostDetailsSerializer

class PostCreateView(generics.CreateAPIView):
    queryset = Post.objects.all().order_by('title')
    serializer_class = PostDetailsSerializer

class PostUpdateView(generics.UpdateAPIView):
    queryset = Post.objects.all().order_by('title')
    serializer_class = PostUpdateSerializer

class PostDestroyView(generics.DestroyAPIView):
    queryset = Post.objects.all().order_by('title')
    serializer_class = PostDetailsSerializer

# Tag
class TagListView(generics.ListAPIView):
    queryset = Tag.objects.all().order_by('name')
    serializer_class = TagListSerializer

class TagRetrieveView(generics.RetrieveAPIView):
    queryset = Tag.objects.all().order_by('name')
    serializer_class = TagDetailsSerializer

class TagCreateView(generics.CreateAPIView):
    queryset = Tag.objects.all().order_by('name')
    serializer_class = TagDetailsSerializer

class TagUpdateView(generics.UpdateAPIView):
    queryset = Tag.objects.all().order_by('name')
    serializer_class = TagDetailsSerializer

class TagDestroyView(generics.DestroyAPIView):
    queryset = Tag.objects.all().order_by('name')
    serializer_class = TagDetailsSerializer
