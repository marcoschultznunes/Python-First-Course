"""
    We'll add a Tag model and it will have a many to many relation to posts
"""

# models.py
from django.db import models
from django.core.validators import MinLengthValidator

class Tag(models.Model):
    name = models.CharField(max_length=40, validators=[MinLengthValidator(2)])

    def __str__(self):
        return self.name 

class Post(models.Model):
    title = models.CharField(max_length=300, validators=[MinLengthValidator(2)])
    content = models.CharField(max_length=3000, validators=[MinLengthValidator(1)])

    # relation here
    tags = models.ManyToManyField(
        "Tag", verbose_name=("posts_tags"), related_name='posts', blank=True
    )

    def __str__(self):
        return self.title
