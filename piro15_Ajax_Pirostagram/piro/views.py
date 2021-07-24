from django.shortcuts import render
from .models import Post, Comment

# Create your views here.
def post_list(request):
    list = Post.objects.all()
    comments = Comment.objects.all()
    ctx = {
        "list": list,
        "comments":comments,
    }
    return render(request, 'piro/post_list.html', ctx)

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    ctx = {
        "post": post,
    }
    return render(request, 'piro/post_detail.html', ctx)

def post_create(request):
    pass

def post_update(request, pk):
    pass

def post_delete(request, pk):
    pass

def comment_ajax(request):
    pass

def like_ajax(request):
    pass