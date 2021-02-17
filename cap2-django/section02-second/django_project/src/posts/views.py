from django.shortcuts import render
from rest_framework import viewsets
from .serializers import (
    PostDetailsSerializer, PostListSerializer, PostUpdateSerializer, 
    TagDetailsSerializer, TagListSerializer
)
from .models import Post, Tag

class PostViewset(viewsets.ModelViewSet):
    def get_serializer_class(self):
        if self.action == 'update' or self.action == 'partial_update':
            return PostUpdateSerializer
        else:
            return PostDetailsSerializer

    queryset = Post.objects.all().order_by('title')
    
class TagViewSet(viewsets.ModelViewSet):
    def get_serializer_class(self):
        if self.action == 'list':
            return TagListSerializer
        else:
            return TagDetailsSerializer

    queryset = Tag.objects.all().order_by('name')
