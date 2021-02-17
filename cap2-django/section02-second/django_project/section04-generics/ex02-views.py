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

class PostCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all().order_by('title')
    serializer_class = PostDetailsSerializer

class PostUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all().order_by('title')
    serializer_class = PostUpdateSerializer

class PostDestroyView(generics.RetrieveDestroyAPIView):
    queryset = Post.objects.all().order_by('title')
    serializer_class = PostDetailsSerializer

# Tag
class TagListView(generics.ListAPIView):
    queryset = Tag.objects.all().order_by('name')
    serializer_class = TagListSerializer

class TagRetrieveView(generics.RetrieveAPIView):
    queryset = Tag.objects.all().order_by('name')
    serializer_class = TagDetailsSerializer

class TagCreateView(generics.ListCreateAPIView):
    queryset = Tag.objects.all().order_by('name')
    serializer_class = TagDetailsSerializer

class TagUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Tag.objects.all().order_by('name')
    serializer_class = TagDetailsSerializer

class TagDestroyView(generics.RetrieveDestroyAPIView):
    queryset = Tag.objects.all().order_by('name')
    serializer_class = TagDetailsSerializer
