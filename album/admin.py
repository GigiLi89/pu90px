from django.contrib import admin
from .models import Post, Comment, Category, Profile
from django_summernote.admin import SummernoteModelAdmin


# From CI
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status', 'display_image')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

    def display_image(self, obj):
        return obj.image.url if obj.image else None
    display_image.short_description = 'Image'


# Register your models here.
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Profile)
