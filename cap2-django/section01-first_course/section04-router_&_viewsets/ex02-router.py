# On Django Rest Framework routes: https://www.youtube.com/watch?v=1k0fRG098cU


# The rest_framework provides a router for us to use. We'll create a file called router.py
from rest_framework import routers
from app.viewsets import UserViewSet

router = routers.DefaultRouter()

router.register('users', UserViewSet, basename='users')


# Then we'll import it to urls.py and we'll place it in a path()
from django.contrib import admin
from django.urls import path, include # We need this include function
from .router import router
from app.views import hello

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello', hello),
    path('app/', include(router.urls)) # routes are now 'app/'
]
