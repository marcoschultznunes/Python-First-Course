from rest_framework import serializers
from .models import Post, Tag

class PostListSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField

    class Meta:
        model = Post
        fields = ('id', 'url', 'title', 'content')

class TagListSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField

    class Meta:
        model = Tag
        fields = ('id', 'url', 'name')

class PostDetailsSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField
    tags = TagListSerializer(read_only=True, many=True)
    
    class Meta: 
        model = Post
        fields = ('id', 'url', 'title', 'content', 'tags')

class TagDetailsSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField
    posts = PostListSerializer(read_only=True, many=True)

    class Meta:
        model = Tag
        fields = ('id', 'name', 'posts')
