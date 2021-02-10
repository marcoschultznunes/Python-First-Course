# https://www.django-rest-framework.org/tutorial/6-viewsets-and-routers/

"""
    Because pylint is a bitch we'll have to install pylint-django.

    pip3 install pylint-django

    Then adjust the settings like the ex01-pylint_django.png shows.
"""

# Viewsets are a different type of views specific of rest_framework. We must pass
# them to the router instead of normal views. They behave like CONTROLLERS.

# In order to make a viewset we need a model and its serializer (i'll explore serializers later).


# serializers.py
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


# viewsets.py
from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


"""
    A viewset provides the 5 basic CRUD operations:

        list() = index
        retreive() = getById
        create() = post
        update() = update
        destroy() = delete

    This means the viewset will provide the 5 routes automatically when added to the router:
        GET /users
        GET /users/:id
        POST /users
        PUT /users/:id
        DELETE /users/:id
"""

"""
@action decorators => allows us to create more endpoints for a viewset

Notice that we've also used the @action decorator to create a custom action, named highlight. 
This decorator can be used to add any custom endpoints that don't fit into the standard 
create/update/delete style.

Custom actions which use the @action decorator will respond to GET requests by default. 
We can use the methods argument if we wanted an action that responded to POST requests.
"""

# APIViews: Are an alternative to viewsets. They allow more control.
#
# APIView vs viewsets:
# https://stackoverflow.com/questions/41379654/difference-between-apiview-class-and-viewsets-class#:~:text=APIView%20allow%20us%20to%20define,%2C%20RETRIEVE%2C%20UPDATE%2C%20etc.
