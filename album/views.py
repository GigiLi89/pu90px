from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from .models import Post, Category, Comment
from .forms import CommentForm
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import Http404


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "album/index.html"
    paginate_by = 6

def post_detail(request, slug):
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()
    
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Thank you! Your comment is submitted and awaiting approval'
            )
    else:
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
        context['categories'] = Category.objects.all()
        return context

def comment_edit(request, slug, comment_id):
    if request.method == "POST":
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))

def comment_delete(request, slug, comment_id):
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


@login_required
def profile(request):
    return render(request, 'account/profile.html')


@login_required
def delete_profile(request):
    user = request.user
    if user.is_authenticated:
        print('User is logged In')
        # TODO: Write your delete logic here
        user.delete()
        
    return HttpResponse("Account Deleted...")
