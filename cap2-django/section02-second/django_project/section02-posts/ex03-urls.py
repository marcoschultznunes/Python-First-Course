# First i'll create the Post app urls.py
from django.urls import path, include
from rest_framework import routers
from .views import PostViewset

router = routers.DefaultRouter()
router.register('posts', PostViewset)

urlpatterns = [
    path('', include(router.urls))
]

# Then i'll add the Post app urls to the project urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/',  include('posts.urls'))
]

"""
    Now we can access the posts endpoints through blog/posts

    Note: I should have named the app blog instead of posts
"""
