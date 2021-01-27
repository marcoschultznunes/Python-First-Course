from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

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
