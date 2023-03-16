from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import Post,Comment


def index(request):
    # body
    return HttpResponse('Wellcome')

def post_list(request):
    posts = Post.objects.all()
    context = {"posts" : posts}
    return  render(request,"posts/list.html",context=context)

def post_detail(request,post_id):
    post = Post.objects.get(pk=post_id)
    comments = Comment.objects.filter(post=post)
    context = {"post" : post , 'comments' : comments}
    return  render(request,"posts/detail.html",context=context)