"""
    Viewsets provide a few classes to extend from.

    Until now we used the ModelViewSet class, but there is also the regular ViewSet, and 
    the GenericViewSet classes.

    ModelViewSet => Automatically provides the 5 actions according to the given model and
    serializer.

    regular ViewSet class => doesn't require model or serializer to be provided. Does not
    automatically program the 5 actions, the programmer implements the ones he wants. The
    regular ViewSet class gives the programmer total control over the viewset but he must
    code everything.

    GenericViewSet => provides the default set of get_object, get_queryset methods and other 
    generic view base behavior, but does not include any actions by default.

"""

# ViewSet
from rest_framework.response import Response

class RegularViewSet(viewsets.ViewSet):
    def list(self, request):
        return Response({'message': 'The angel from my nightmare'})


# ModelViewSet
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
