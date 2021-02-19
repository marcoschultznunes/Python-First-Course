# On the post model
class Post(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# python manage.py makemigrations
# python manage.py migrate

"""
    Finally, we must add created_at and updated_at to the serializers.
    We won't add it to the save serializer
"""
