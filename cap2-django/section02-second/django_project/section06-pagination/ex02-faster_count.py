"""
    https://stackoverflow.com/questions/31740039/django-rest-framework-pagination-extremely-slow-count

    The query used to count is the same complex one used to fetch the data. This makes
    the pagination slow to count. If there are millions or more entries in the database,
    the count will make any request very slow.

    In this example, we'll override the default count function.
"""
from rest_framework.pagination import PageNumberPagination
from django.core.paginator import Paginator
from django.utils.functional import cached_property

class FasterDjangoPaginator(Paginator): # Make a custom paginator class
    @cached_property
    def count(self):
        # only select 'id' for counting, much cheaper
        return self.object_list.values('id').count()

class StandardResultsSetPagination(PageNumberPagination):
    django_paginator_class = FasterDjangoPaginator # set this attribute to the paginator class
    page_size = 50
    page_size_query_param = 'perPage'
    max_page_size = 200
