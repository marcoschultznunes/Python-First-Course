from rest_framework.pagination import PageNumberPagination

class StandardResultsSetPagination(PageNumberPagination): # Pagination config class
    page_size = 50
    page_size_query_param = 'perPage'
    max_page_size = 200

class PostViewset(viewsets.ModelViewSet):
    def get_serializer_class(self):
        if self.action == 'update' or self.action == 'partial_update' or self.action == 'create':
            return PostSaveSerializer
        else:
            return PostDetailsSerializer

    queryset = Post.objects.all().order_by('title')
    pagination_class = StandardResultsSetPagination # Just add it as an attribute to the viewset
    
class TagViewSet(viewsets.ModelViewSet):
    def get_serializer_class(self):
        if self.action == 'list':
            return TagListSerializer
        else:
            return TagDetailsSerializer

    queryset = Tag.objects.all().order_by('name')
    pagination_class = StandardResultsSetPagination # Can be reused

"""
    Request example:

        http://127.0.0.1:8000/blog/posts/?perPage=2

        {
            "count": 3,
            "next": "http://127.0.0.1:8000/blog/posts/?page=2&perPage=2",
            "previous": null,
            "results": [
                {
                    "id": 3,
                    "url": "http://127.0.0.1:8000/blog/posts/3/",
                    "title": "VTNC",
                    "content": "POHA",
                    "tags": [
                        {
                            "id": 2,
                            "url": "http://127.0.0.1:8000/blog/tags/2/",
                            "name": "LOL"
                        },
                        {
                            "id": 3,
                            "url": "http://127.0.0.1:8000/blog/tags/3/",
                            "name": "NEW"
                        }
                    ]
                },
                {
                    "id": 2,
                    "url": "http://127.0.0.1:8000/blog/posts/2/",
                    "title": "Vtnc",
                    "content": "Ah va a merda poha!",
                    "tags": []
                }
            ]
        }
"""
