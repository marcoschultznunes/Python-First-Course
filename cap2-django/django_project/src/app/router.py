from rest_framework import routers
from .viewsets import UserViewSet, TagViewSet, PostViewSet, AccountViewSet

router = routers.DefaultRouter()

router.register('users', UserViewSet)
router.register('tags', TagViewSet)
router.register('posts', PostViewSet)
router.register('accounts', AccountViewSet)
