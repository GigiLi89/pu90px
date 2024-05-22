from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post, Category
from .forms import CommentForm

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "album/index.html"
    paginate_by = 6

def post_detail(request, slug):
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()
    comment_form = CommentForm()

    return render(request, "album/post_detail.html", {
        "post": post,
        "coder": "PU90PX",  
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form,
    })


class CategoryList(generic.ListView):
    template_name = 'base.html'
    context_object_name = 'posts'

    def get_queryset(self):
        category = self.kwargs['category']
        return Post.objects.filter(categories__name=category, status=1)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_list'] = Category.objects.exclude(name='default')

        # Pass categories to the template context
        context['categories'] = Category.objects.all()
        return context
