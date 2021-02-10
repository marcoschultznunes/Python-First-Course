# Serializer
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


# Viewset
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# Router
router.register('posts', PostViewSet, basename='posts')

"""
    POST Request:

    {
        "title": "Some shit",
        "content": "Bla bla bla",
        "user_id": 5,
        "tags": [
            3,
            4
        ]
    }


    Response:

    {
        "id": 4,
        "title": "Some shit",
        "content": "Bla bla bla",
        "created_at": "2021-01-29T07:25:36.456659Z",
        "updated_at": "2021-01-29T07:25:36.456716Z",
        "user_id": 5,
        "tags": [
            3,
            4
        ]
    }
"""