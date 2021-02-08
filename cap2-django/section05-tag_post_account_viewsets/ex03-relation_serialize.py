"""
    We can serialize relations turning them into links (IDs too) by doing the following:

    1 - Removing all basename attributes from the router
"""
router.register('users', UserViewSet)
router.register('tags', TagViewSet)
router.register('posts', PostViewSet)
router.register('accounts', AccountViewSet)

# 2 - Making the serializers extend serializers.HyperlinkedModelSerializer
class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class AccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

"""
    example:

    GET posts

    [
        {
            "url": "http://127.0.0.1:8000/app/posts/1/",
            "title": "What the fu?",
            "content": "Hello, i'm Cory in the house.",
            "created_at": "2021-01-26T05:13:46.270909Z",
            "updated_at": "2021-01-26T05:13:46.281614Z",
            "user_id": "http://127.0.0.1:8000/app/users/1/",
            "tags": [
                "http://127.0.0.1:8000/app/tags/2/",
                "http://127.0.0.1:8000/app/tags/4/"
            ]
        },
        {
            "url": "http://127.0.0.1:8000/app/posts/2/",
            "title": "Book of Love",
            "content": "I don't know what planet i'm on man",
            "created_at": "2021-01-26T05:13:46.270909Z",
            "updated_at": "2021-01-26T05:13:46.281614Z",
            "user_id": "http://127.0.0.1:8000/app/users/1/",
            "tags": [
                "http://127.0.0.1:8000/app/tags/1/"
            ]
        },
        {
            "url": "http://127.0.0.1:8000/app/posts/3/",
            "title": "Everybody in Uganda knows kung fu!",
            "content": "Hello, i'm Cory in the house.",
            "created_at": "2021-01-26T05:13:46.270909Z",
            "updated_at": "2021-01-26T05:13:46.281614Z",
            "user_id": "http://127.0.0.1:8000/app/users/1/",
            "tags": [
                "http://127.0.0.1:8000/app/tags/2/",
                "http://127.0.0.1:8000/app/tags/3/"
            ]
        },
        {
            "url": "http://127.0.0.1:8000/app/posts/4/",
            "title": "Some shit",
            "content": "Bla bla bla",
            "created_at": "2021-01-29T07:25:36.456659Z",
            "updated_at": "2021-01-29T07:25:36.456716Z",
            "user_id": "http://127.0.0.1:8000/app/users/5/",
            "tags": [
                "http://127.0.0.1:8000/app/tags/3/",
                "http://127.0.0.1:8000/app/tags/4/"
            ]
        }
    ]


One cost of HyperlinkedModelSerializers that should be noted is that if your API supports 
filtering or ordering via query parameters in the URL it is a bit more difficult for your 
frontend consumer to use the hyperlinked url fields for constructing query params because they 
have to parse out the pk from the URL rather than having the pk directly available
"""
