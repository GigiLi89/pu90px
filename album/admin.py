from django.contrib import admin
from .models import Post, Comment

# Register your models here.

# Allow us to create, edit and delete posts
admin.site.register(Post)
admin.site.register(Comment)