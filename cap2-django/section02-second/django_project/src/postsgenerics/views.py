from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from posts.models import Post, Tag
from posts.serializers import (
    PostDetailsSerializer, PostListSerializer, PostUpdateSerializer, 
    TagDetailsSerializer, TagListSerializer
)

# Post
class PostListView(generics.ListAPIView):
    queryset = Post.objects.all().order_by('title')
    serializer_class = PostListSerializer

class PostRetrieveView(generics.RetrieveAPIView):
    queryset = Post.objects.all().order_by('title')
    serializer_class = PostDetailsSerializer

class PostCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all().order_by('title')
    serializer_class = PostDetailsSerializer

class PostUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all().order_by('title')
    serializer_class = PostUpdateSerializer

    def patch(self, request, pk):
        post = get_object_or_404(Post, pk=pk) # imported from django.shortcuts
        serializer = PostUpdateSerializer(post, data=request.data, partial=True, context={'request': request})

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        # return a meaningful error response
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostDestroyView(generics.RetrieveDestroyAPIView):
    queryset = Post.objects.all().order_by('title')
    serializer_class = PostDetailsSerializer

# Tag
class TagListView(generics.ListAPIView):
    queryset = Tag.objects.all().order_by('name')
    serializer_class = TagListSerializer

class TagRetrieveView(generics.RetrieveAPIView):
    queryset = Tag.objects.all().order_by('name')
    serializer_class = TagDetailsSerializer

class TagCreateView(generics.ListCreateAPIView):
    queryset = Tag.objects.all().order_by('name')
    serializer_class = TagDetailsSerializer

class TagUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Tag.objects.all().order_by('name')
    serializer_class = TagDetailsSerializer

class TagDestroyView(generics.RetrieveDestroyAPIView):
    queryset = Tag.objects.all().order_by('name')
    serializer_class = TagDetailsSerializer
