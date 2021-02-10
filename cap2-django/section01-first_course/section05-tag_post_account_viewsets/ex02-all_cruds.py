# Serializer
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'

# Viewset
class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

# Router
router.register('tags', TagViewSet, basename='tags')
router.register('posts', PostViewSet, basename='posts')
router.register('accounts', AccountViewSet, basename='accounts')

"""
    As you can see, Django can be extremely quick to develop, saving a ton of time, and tons 
    of lines of code. 
"""
