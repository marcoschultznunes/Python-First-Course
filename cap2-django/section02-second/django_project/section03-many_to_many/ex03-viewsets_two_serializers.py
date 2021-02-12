"""
    In this example, we'll make the viewsets use the list serializer for listing and the
    details serializer for get by id, update and delete.

    To do this, we'll override the get_serializer_class(self) function.
"""

# views.py 
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import (
    PostDetailsSerializer, PostListSerializer, TagDetailsSerializer, TagListSerializer
)
from .models import Post, Tag

class PostViewset(viewsets.ModelViewSet):

    # We simply add conditional logic to this function returning the serializer
    def get_serializer_class(self):
        if self.action == 'list':
            return PostListSerializer
        else:    
            return PostDetailsSerializer

    queryset = Post.objects.all().order_by('title')
    # Don't forget to erase serializer_class = PostDetailsSerializer!
    
class TagViewSet(viewsets.ModelViewSet):
    def get_serializer_class(self):
        if self.action == 'list':
            return TagListSerializer
        else:
            return TagDetailsSerializer

    queryset = Tag.objects.all().order_by('name')

