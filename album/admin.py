from django.contrib import admin
from .models import Post

# Register your models here.

# Allow us to create, edit and delete posts
admin.site.register(Post)

