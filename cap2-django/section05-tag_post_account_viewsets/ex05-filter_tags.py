"""
    In this example, we'll add an action to the posts viewset which will fetch posts given 
    an array of tags passed as a query param
"""

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @action(methods=['GET'], detail=False, url_path='tags', url_name='tags') # posts/tags
    def posts_by_tags(self, request):
        tags = request.GET.getlist('tags') # Gets the tags array from the query

        posts = Post.objects.all().filter(tags__in=tags) # Filters the posts with any of the tags
        serializedPosts = self.get_serializer(posts, many=True)

        return Response({'posts': serializedPosts.data})

"""
    Sample request:

    http://127.0.0.1:8000/app/posts/tags/?tags=2&tags=1

    Response:

    {
        "posts": [
            {
                "id": 2,
                "url": "http://127.0.0.1:8000/app/posts/2/",
                "title": "Book of Love",
                "content": "I don't know what planet i'm on man",
                "tags": [
                    "http://127.0.0.1:8000/app/tags/1/"
                ],
                "created_at": "2021-01-26T05:13:46.270909Z",
                "updated_at": "2021-01-26T05:13:46.281614Z"
            },
            {
                "id": 3,
                "url": "http://127.0.0.1:8000/app/posts/3/",
                "title": "Everybody in Uganda knows kung fu!",
                "content": "Hello, i'm Cory in the house.",
                "tags": [
                    "http://127.0.0.1:8000/app/tags/2/",
                    "http://127.0.0.1:8000/app/tags/3/"
                ],
                "created_at": "2021-01-26T05:13:46.270909Z",
                "updated_at": "2021-01-26T05:13:46.281614Z"
            },
            {
                "id": 1,
                "url": "http://127.0.0.1:8000/app/posts/1/",
                "title": "What the fu?",
                "content": "Hello, i'm Cory in the house.",
                "tags": [
                    "http://127.0.0.1:8000/app/tags/2/",
                    "http://127.0.0.1:8000/app/tags/4/"
                ],
                "created_at": "2021-01-26T05:13:46.270909Z",
                "updated_at": "2021-01-26T05:13:46.281614Z"
            }
        ]
    }
"""
