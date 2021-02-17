"""
    The solution is to create a PostSaveSerializer,
    and have it serialize the tags a list of ids with:
        tags = serializers.PrimaryKeyRelatedField(queryset=Tag.objects.all(), many=True)
"""

# On serializers.py
class PostSaveSerializer(serializers.HyperlinkedModelSerializer):
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

        # Note: partial_update for PATCH
        if self.action == 'update' or self.action == 'partial_update' or self.action == 'create':
            return PostSaveSerializer
        else:
            return PostDetailsSerializer

    queryset = Post.objects.all().order_by('title')


"""
    Now we can update and create posts by sending a JSON requests, passing the tag ids on a 
    'tags' list:

    PATCH /blog/posts/1

    {
        "tags": [
            2,
            3
        ]
    }

    Note: PATCH action is called partial_update in Django
"""
