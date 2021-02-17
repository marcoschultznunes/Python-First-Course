from rest_framework import serializers
from .models import Post, Tag

# List
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

# Details
class PostDetailsSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField
    tags = TagListSerializer(read_only=False, many=True)
    
    class Meta: 
        model = Post
        fields = ('id', 'url', 'title', 'content', 'tags')

class TagDetailsSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField
    posts = PostListSerializer(read_only=True, many=True)

    class Meta:
        model = Tag
        fields = ('id', 'name', 'posts')

# Update and create - many to many
class PostSaveSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField
    tags = serializers.PrimaryKeyRelatedField(queryset=Tag.objects.all(), many=True)

    class Meta:
        model = Post
        fields = ('id', 'url', 'title', 'content', 'tags')
