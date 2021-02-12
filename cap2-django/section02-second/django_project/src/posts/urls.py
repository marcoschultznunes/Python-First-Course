from django.urls import path, include
from rest_framework import routers
from .views import PostViewset, TagViewSet

router = routers.DefaultRouter()

router.register('posts', PostViewset)
router.register('tags', TagViewSet)

urlpatterns = [
    path('', include(router.urls))
]
