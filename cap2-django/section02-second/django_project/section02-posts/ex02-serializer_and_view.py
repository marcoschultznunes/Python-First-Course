# Create the serializers.py file
from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField

    class Meta: 
        model = Post
        fields = ('id', 'url', 'title', 'content')

# views.py
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PostSerializer
from .models import Post

class PostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('title')
    serializer_class = PostSerializer
    