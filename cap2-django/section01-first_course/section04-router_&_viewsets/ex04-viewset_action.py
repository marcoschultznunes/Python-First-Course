"""
    We can add custom actions to our viewsets by using the @action decorator
"""

# viewsets.py
from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer
from rest_framework.decorators import action # action must be imported
from rest_framework.response import Response

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # detail => if true, should return a single object, if false should return a list.
    @action(methods=["get"], detail=True, url_path="test", url_name="test")
    def test(self, request):
        return Response({'message': 'Hello There'}, status=204)


    # Second example: order by name
    @action(methods=["get"], detail=False, url_path="sorted", url_name="sorted")
    def users_sort_by_name(self, request):
        
        users = self.queryset.order_by('name') # gets and orders by name

        serializedUsers = self.get_serializer(users, many=True) # serializes

        return Response({'users': serializedUsers.data}) 

"""
    Note:
        queryset = User.objects.all()

        queryset is just the list of all the database elements of the given model.
        Its value can be modified to have pagination, orderBy, etc.

    Note 2:
        The way you name the function will change the function name displayed in the browser.
        For instance: users_sort_by_name => Users sort by name

"""
