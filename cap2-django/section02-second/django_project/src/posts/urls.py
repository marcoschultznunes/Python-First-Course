from django.urls import path, include
from rest_framework import routers
from .views import PostViewset

router = routers.DefaultRouter()

router.register('posts', PostViewset)

urlpatterns = [
    path('', include(router.urls))
]
