from django.db import models

class User(models.Model):
    name = models.CharField(max_length = 150)
    email = models.CharField(max_length = 100)
    password = models.CharField(max_length = 40)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

    class Meta:
        db_table = "users"


class Tag(models.Model):
    name = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = "tags"



class Post(models.Model):
    title = models.CharField(max_length = 200)
    content = models.CharField(max_length=3000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    user_id = models.ForeignKey("User", on_delete = models.CASCADE)

    tags = models.ManyToManyField("Tag")

    def __str__(self):
        return self.title

    class Meta:
        db_table = "posts"


class Account(models.Model):
    login = models.CharField(max_length=100)
    verified = models.BooleanField(default=False)
    user_id = models.OneToOneField("User", on_delete = models.CASCADE)

    def __str__(self):
        return self.login

    class Meta:
        db_table = "accounts"

