"""
    The solution to the problem of serializing many to many relations is to make more 
    serializers.
"""

# serializers.py
class PostListSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField

    class Meta:
        model = Post
        fields = ('id', 'url', 'title', 'content')

class TagListSerializer(serializers.HyperlinkedModelSerializer):
    # This serializer is necessary so that we can bring the tags to the post instead of
    # only retreiving the IDs.
    # This way we can use: tags = TagListSerializer(read_only=True, many=True)
    # in the serializer that we'll use to display the post with its tags.

    id = serializers.ReadOnlyField

    class Meta:
        model = Tag
        fields = ('id', 'url', 'name')

class PostDetailsSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField
    tags = TagListSerializer(read_only=True, many=True) # Thanks to the previous serializer
    
    class Meta: 
        model = Post
        fields = ('id', 'url', 'title', 'content', 'tags')

class TagDetailsSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField
    posts = PostListSerializer(read_only=True, many=True)

    class Meta:
        model = Tag
        fields = ('id', 'name', 'posts')

"""
    Note: There is one problem with this serializer that we are not addressing yet, which is 
    updating the post's tags. We will solve this in ex04.
"""

# views.py, using the details serializer
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PostDetailsSerializer, TagDetailsSerializer
from .models import Post, Tag

class PostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('title')
    serializer_class = PostDetailsSerializer
    
class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all().order_by('name')
    serializer_class = TagDetailsSerializer
