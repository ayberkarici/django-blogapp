#http://127.0.0.1:8000/

from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"), ### name ==> views/index called home
    path("index", views.index), 
    path("blogs", views.blogs, name="blogs"), ### name ==> views/blogs called blogs
    path("blogs/<slug:slug>", views.blog_details, name="blog_details"),  ### name ==> views/blog_details called blog_details
    path("category/<slug:slug>", views.blogs_by_category, name="blogs_by_category"),  ### name ==> views/blog_details called blog_details
]