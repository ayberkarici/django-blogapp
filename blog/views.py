from pickle import FALSE
from unicodedata import category
from django.shortcuts import redirect, render
from django.http.response import HttpResponse
from django.shortcuts import render
from blog.models import Blog
from blog.models import Category

def index(request):
    
    context = {
        "blogs" : Blog.objects.filter(isActive=True, isHome=True),
        "categories" : Category.objects.all()
    }
    return render(request, "blog/index.html", context)


def blogs(request):
    context = {
        "blogs" : Blog.objects.filter(isActive=True),
        "categories" : Category.objects.all()
    }
    return render(request, "blog/blogs.html", context)


def blog_details(request, slug):
    blog = Blog.objects.get(slug=slug)
    
    return render(request, "blog/blog-detail.html", {
        "blog" : blog
    })
    
def blogs_by_category(request, slug):
    context = {
        "blogs" : Category.objects.get(slug = slug).blog_set.filter(isActive = True),
        #"blogs" : Blog.objects.filter(isActive=True, category__slug=slug),
        "categories" : Category.objects.all(),
        "selected_category" : slug,
    }
    return render(request, "blog/blogs.html", context)
