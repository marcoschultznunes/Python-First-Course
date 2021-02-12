"""
    The solution is to create a PostUpdateSerializer,
    and have it serialize the tags a list of ids with:
        tags = serializers.PrimaryKeyRelatedField(queryset=Tag.objects.all(), many=True)
"""

# On serializers.py
class PostUpdateSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField
    tags = serializers.PrimaryKeyRelatedField(queryset=Tag.objects.all(), many=True)

    class Meta:
        model = Post
        fields = ('id', 'url', 'title', 'content', 'tags')

"""
    Then, we add the serializer conditional logic on the view
"""

# On views.py
class PostViewset(viewsets.ModelViewSet):
    def get_serializer_class(self):
        if self.action == 'update':
            return PostUpdateSerializer
        else:
            return PostDetailsSerializer

    queryset = Post.objects.all().order_by('title')


"""
    Now we can update the post by sending a JSON request, passing the tag ids on a 'tags' list:

    PUT /blog/posts/1

    {
        "id": 1,
        "url": "http://127.0.0.1:8000/blog/posts/1/",
        "title": "What the fu?",
        "content": "Q",
        "tags": [
            2,
            3
        ]
    }
"""
