"""
    We can also delete the count attribute.
"""

from collections import OrderedDict
from rest_framework.response import Response

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 50
    page_size_query_param = 'perPage'
    max_page_size = 200

    # We override the response, without including the count field.
    def get_paginated_response(self, data): 
        return Response(OrderedDict([
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('results', data)
        ]))
