from django.contrib import admin
from django.urls import path, include
from .router import router
from app.views import hello

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello', hello),
    path('app/', include(router.urls))
]
