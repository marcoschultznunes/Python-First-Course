from rest_framework import serializers
from .models import User, Tag, Post, Account

class PostSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField

    class Meta:
        model = Post
        fields = ['id', 'url', 'title', 'content', 'tags', 'created_at', 'updated_at']

class TagSerializer(serializers.HyperlinkedModelSerializer):
    posts = PostSerializer(many=True, read_only=True)

    # FUCKING MANY TO MANY SERIALIZER BULLSHIT FUCK THIS SHIT WHY DOES IT NOT WORK FUCK

    id = serializers.ReadOnlyField

    class Meta:
        model = Tag
        fields = ['id', 'url', 'name', 'posts']

class AccountSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField

    class Meta:
        model = Account
        fields = ['id', 'url', 'login', 'verified', 'user_id']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    account = AccountSerializer(many=False, read_only=True)
    id = serializers.ReadOnlyField

    class Meta:
        model = User
        fields = [
            'id', 'url', 'name', 'email', 'password', 'account', 'created_at', 'updated_at'
        ]
