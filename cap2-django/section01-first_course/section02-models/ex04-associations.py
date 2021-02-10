"""
    To work with associations we'll add posts, which will have a many to one relation with
    users, then accounts, which will have a one to one relation with users, 
    and then tags, which will have a many to many relation with posts
"""
from django.db import models

class User(models.Model):
    name = models.CharField(max_length = 150) # String
    email = models.CharField(max_length = 100)
    password = models.CharField(max_length = 40)

    def __str__(self): # toString => Useful for displaying in admin panel
        return self.email

    class Meta:
        db_table = "users" # Table name
        

class Tag(models.Model):
    name = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = "tags"


class Post(models.Model):
    title = models.CharField(max_length = 200)
    content = models.CharField(max_length=3000)

    # Many to one association
    user_id = models.ForeignKey("User", on_delete = models.CASCADE) # on_delete is always required

    # Many to many association
    tags = models.ManyToManyField("Tag")

    def __str__(self):
        return self.title

    class Meta:
        db_table = "posts"


class Account(models.Model):
    login = models.CharField(max_length=100)
    verified = models.BooleanField(default=False)

    # One to one association
    user_id = models.OneToOneField("User", on_delete = models.CASCADE)
    
    def __str__(self):
        return self.login

    class Meta:
        db_table = "accounts"

