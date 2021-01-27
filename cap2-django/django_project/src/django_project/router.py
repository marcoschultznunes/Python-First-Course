from rest_framework import routers
from app.viewsets import UserViewSet

router = routers.DefaultRouter()

router.register('users', UserViewSet, basename='users')
