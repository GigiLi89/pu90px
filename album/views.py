from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "album/index.html"
    paginate_by = 6


def album(request):
    return render(request, 'album.html')