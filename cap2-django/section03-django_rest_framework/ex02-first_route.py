"""
    We'll now add the first route to our API, which will return the message "Hello There".

    For this, we'll need to add a view.
"""

# views.py
from django.http import JsonResponse
from django.shortcuts import render

def hello(req):
    res = {
        'message': 'Hello There'
    }

    return JsonResponse(res)


# urls.py
from django.contrib import admin
from django.urls import path
"from app.views import hello" # views are imported from app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello', hello) # no slash before first folder
]
