from django.shortcuts import render,get_object_or_404
from datetime import date

from .models import *

# Create your views here

def starting_page(request):
    latest_posts = posts = Post.objects.all().order_by("-date")[:3]
    
    context={
        "posts":latest_posts
    }
    return render(request, 'blog/index.html',context)
def posts(request):
    all_posts = Post.objects.all().order_by("-date")
    context={
        "all_posts":all_posts
    }
    return render(request,'blog/all-posts.html',context)

def post_detail(request,slug):

    identified_post = get_object_or_404(Post,slug=slug)
    context={
        "post":identified_post,
        "post_tags":identified_post.tag.all()
    }
    return render(request,'blog/post-detail.html',context)
