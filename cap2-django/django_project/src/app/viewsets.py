from rest_framework import viewsets
from .models import User, Tag, Post, Account
from .serializers import UserSerializer, TagSerializer, PostSerializer, AccountSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @action(methods=['GET'], detail=False, url_path='tags', url_name='tags')
    def posts_by_tags(self, request):
        tags = request.GET.getlist('tags')

        posts = Post.objects.all().filter(tags__in=tags)
        serializedPosts = self.get_serializer(posts, many=True)

        return Response({'posts': serializedPosts.data})

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request):
        users = self.queryset.order_by('name')

        serializedUsers = self.get_serializer(users, many=True)

        return Response({'users': serializedUsers.data})


    @action(methods=["get"], detail=True, url_path="test", url_name="test")
    def test(self, request):
        return Response({'message': 'Hello There'}, status=204)


    @action(methods=["get"], detail=False, url_path="sorted", url_name="sorted")
    def users_sort_by_name(self, request):
        
        users = self.queryset.order_by('name')

        serializedUsers = self.get_serializer(users, many=True)

        return Response({'users': serializedUsers.data})
