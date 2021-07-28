from django.shortcuts import redirect, render
from .models import Post, Comment
from .forms import PostForm
import json
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

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

@csrf_exempt
def like_ajax(request):
    req = json.loads(request.body)
    post_id = req['id']

    post = Post.objects.get(id=post_id)

    if post.like == 0:
        post.like += 1
    else :
        post.like -= 1

    post.save()
    return JsonResponse({'id': post_id})

@csrf_exempt
def comment_write(request, pk):
    req = json.loads(request.body)
    post_id = req['id']
    button_type = req['type']
    comment_content = req['content']

    current_post = Post.objects.get(id=post_id)
    comments = Comment.objects.filter(post=current_post)

    if button_type == 'write':
        comments.content = comment_content
    else:
        pass
    current_post.save()
    comments.save()
    return JsonResponse({'id': post_id, 'content': comment_content})

    
    
