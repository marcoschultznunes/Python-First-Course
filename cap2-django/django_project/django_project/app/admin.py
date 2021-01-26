from django.contrib import admin

from .models import User, Post, Account, Tag

admin.site.register(User)
admin.site.register(Post)
admin.site.register(Account)
admin.site.register(Tag)
