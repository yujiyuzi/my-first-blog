from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    #posts = Post.objects.filter(id=1)
    # posts = "aaaaaaaaaaaa"
    #print('printprint')
    return render(gitrequest, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    return render(request, 'blog/post_detail.html', {'post': post})



#from django.shortcuts import render
#from django.utils import timezone
#from blog.models import Post
#
#import requests
#
#def post_list(request):
    #    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    #context ={
    #    'posts': posts
    #}
    #return render(requests, "blog/templates/blog/post_list.html", context)