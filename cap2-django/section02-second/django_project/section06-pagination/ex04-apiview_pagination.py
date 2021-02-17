"""
    It's the same as we already did, but we add the paginator class to each apiview.

    Instead of django_paginator_class, the attribute is called
    pagination_class.
"""

from rest_framework.pagination import PageNumberPagination
from django.core.paginator import Paginator
from django.utils.functional import cached_property

# The paginator with fast count
class FasterDjangoPaginator(Paginator):
    @cached_property
    def count(self):
        return self.object_list.values('id').count()

class StandardResultsSetPagination(PageNumberPagination):
    django_paginator_class = FasterDjangoPaginator 
    page_size = 50
    page_size_query_param = 'perPage'
    max_page_size = 200


# ListAPIView with pagination_class attribute
class PostListView(generics.ListAPIView):
    queryset = Post.objects.all().order_by('title')
    serializer_class = PostListSerializer
    pagination_class = StandardResultsSetPagination
