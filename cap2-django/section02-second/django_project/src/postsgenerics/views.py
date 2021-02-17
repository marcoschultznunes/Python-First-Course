from rest_framework import generics

from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response

from rest_framework.pagination import PageNumberPagination
from django.core.paginator import Paginator
from django.utils.functional import cached_property

from posts.models import Post, Tag
from posts.serializers import (
    PostDetailsSerializer, PostListSerializer, PostSaveSerializer,
    TagDetailsSerializer, TagListSerializer
)

class FasterDjangoPaginator(Paginator):
    @cached_property
    def count(self):
        return self.object_list.values('id').count()

class StandardResultsSetPagination(PageNumberPagination):
    django_paginator_class = FasterDjangoPaginator 
    page_size = 50
    page_size_query_param = 'perPage'
    max_page_size = 200

# Post
class PostListView(generics.ListAPIView):
    queryset = Post.objects.all().order_by('title')
    serializer_class = PostListSerializer
    pagination_class = StandardResultsSetPagination

class PostRetrieveView(generics.RetrieveAPIView):
    queryset = Post.objects.all().order_by('title')
    serializer_class = PostDetailsSerializer

class PostCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all().order_by('title')
    serializer_class = PostSaveSerializer
    pagination_class = StandardResultsSetPagination

class PostUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all().order_by('title')
    serializer_class = PostSaveSerializer

    def patch(self, request, pk):
        post = get_object_or_404(Post, pk=pk) # imported from django.shortcuts
        serializer = PostUpdateSerializer(post, data=request.data, partial=True, context={'request': request})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) # imported from rest_framework.response

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostDestroyView(generics.RetrieveDestroyAPIView):
    queryset = Post.objects.all().order_by('title')
    serializer_class = PostDetailsSerializer

# Tag
class TagListView(generics.ListAPIView):
    queryset = Tag.objects.all().order_by('name')
    serializer_class = TagListSerializer
    pagination_class = StandardResultsSetPagination

class TagRetrieveView(generics.RetrieveAPIView):
    queryset = Tag.objects.all().order_by('name')
    serializer_class = TagDetailsSerializer

class TagCreateView(generics.ListCreateAPIView):
    queryset = Tag.objects.all().order_by('name')
    serializer_class = TagDetailsSerializer
    pagination_class = StandardResultsSetPagination

class TagUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Tag.objects.all().order_by('name')
    serializer_class = TagDetailsSerializer

class TagDestroyView(generics.RetrieveDestroyAPIView):
    queryset = Tag.objects.all().order_by('name')
    serializer_class = TagDetailsSerializer
