"""
    We can also overwrite the 5 default methods of the viewsets, in which case we don't need
    decorators. Reminder of the 5 methods:
        list() = index
        retreive() = getById
        create() = post
        update() = update
        destroy() = delete

    In this example, we'll overwrite list on the user viewset, ordering by name
"""

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


# Now the list action is overwritten. The other actions remain the same, as they were not
# modified.
