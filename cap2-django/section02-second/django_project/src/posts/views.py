from django.shortcuts import render
from rest_framework import viewsets
from .serializers import (
    PostDetailsSerializer, PostListSerializer, TagDetailsSerializer, TagListSerializer
)
from .models import Post, Tag

class PostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('title')
    serializer_class = PostDetailsSerializer
    
class TagViewSet(viewsets.ModelViewSet):
    def get_serializer_class(self):
        if self.action == 'list':
            return TagListSerializer
        else:
            return TagDetailsSerializer

    queryset = Tag.objects.all().order_by('name')
