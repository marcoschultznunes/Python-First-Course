from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
def hello(req):
    res = {
        'message': 'Hello There'
    }

    return JsonResponse(res, status=200)
