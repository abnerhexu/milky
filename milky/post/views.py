from django.shortcuts import render
from .models import OnePost
import markdown


def post_list(request):
    # 从Post中取出所有文章
    posts = OnePost.objects.all()
    context = {'posts': posts}
    return render(request, 'post/list.html', context)

def post_details(request, id):
    post = OnePost.objects.get(id=id)
    post.body = markdown.markdown(post.body,
                                  extensions=['markdown.extensions.extra',
                                              'markdown.extensions.codehilite',
                                              ])
    context = {"post": post}
    return render(request, 'post/detail.html', context)
