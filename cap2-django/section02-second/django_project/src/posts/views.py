from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from django.core.paginator import Paginator
from django.utils.functional import cached_property
from collections import OrderedDict
from rest_framework.response import Response

from .serializers import (
    PostDetailsSerializer, PostListSerializer, PostSaveSerializer, 
    TagDetailsSerializer, TagListSerializer
)
from .models import Post, Tag


# Pagination

class FasterDjangoPaginator(Paginator):
    @cached_property
    def count(self):
        return self.object_list.values('id').count()

class StandardResultsSetPagination(PageNumberPagination):
    django_paginator_class = FasterDjangoPaginator 
    page_size = 50
    page_size_query_param = 'perPage'
    max_page_size = 200

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('results', data)
        ]))


# Viewsets

class PostViewset(viewsets.ModelViewSet):
    def get_serializer_class(self):
        if self.action == 'update' or self.action == 'partial_update' or self.action == 'create':
            return PostSaveSerializer
        else:
            return PostDetailsSerializer

    queryset = Post.objects.all().order_by('title')
    pagination_class = StandardResultsSetPagination
    
class TagViewSet(viewsets.ModelViewSet):
    def get_serializer_class(self):
        if self.action == 'list':
            return TagListSerializer
        else:
            return TagDetailsSerializer

    queryset = Tag.objects.all().order_by('name')
    pagination_class = StandardResultsSetPagination
