from django.urls import path, include
from .views import (
    PostListView, PostRetrieveView, PostCreateView, PostUpdateView, PostDestroyView,
    TagListView, TagRetrieveView, TagCreateView, TagUpdateView, TagDestroyView
)

urlpatterns = [
    path('posts/', PostListView.as_view()),
    path('posts/<int:pk>/', PostRetrieveView.as_view()),
    path('posts/create/', PostCreateView.as_view()),
    path('posts/update/<int:pk>/', PostUpdateView.as_view()),
    path('posts/delete/<int:pk>/', PostDestroyView.as_view()),
    path('Tag/', TagListView.as_view()),
    path('Tag/<int:pk>/', TagRetrieveView.as_view()),
    path('Tag/create/', TagCreateView.as_view()),
    path('Tag/update/<int:pk>/', TagUpdateView.as_view()),
    path('Tag/delete/<int:pk>/', TagDestroyView.as_view()),
]
