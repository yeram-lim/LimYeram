from django.shortcuts import redirect, render
from .models import Post, Comment
from .forms import PostForm


# Create your views here.
def post_list(request):
    list = Post.objects.all()
    ctx = {
        "list": list,
    }
    return render(request, 'piro/post_list.html', ctx)

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    ctx = {
        "post": post,
    }
    return render(request, 'piro/post_detail.html', ctx)

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid:
            post = form.save()
            return redirect('piro:post_list') 
    else:
        form = PostForm()
        ctx = {
            "form": form
        }
        return render(request, 'piro/post_create.html', ctx)

def post_update(request, pk):
    pass

def post_delete(request, pk):
    pass

def comment_ajax(request):
    pass

def like_ajax(request):
    pass