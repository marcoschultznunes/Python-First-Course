# The Post model
from django.db import models
from django.core.validators import MinLengthValidator

class Post(models.Model):
    title = models.CharField(max_length=300, validators=[MinLengthValidator(2)])
    content = models.CharField(max_length=3000, validators=[MinLengthValidator(1)])

    # The following code demonstrates how to redefine the name of the model in plural.
    # For instance, this determines the name displayed on Django Admin.
    class Meta:
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title

# On admin.py
from django.contrib import admin
from .models import Post

admin.site.register(Post)

"""
    Then we must do the migrations:
        python manage.py makemigrations
        python manage.py migrate
"""
