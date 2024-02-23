from django.shortcuts import render
from .models import Post, Category, Tag


def home_view(request):
    posts = Post.objects.filter(is_published=True)
    categories = Category.objects.all()
    tags = Tag.objects.all()
    context = {
        'posts': posts,
        'categories': categories,
        'tags': tags
    }
    return render(request, 'index.html', context=context)


def about_view(request):
    posts = Post.objects.filter(is_published=True)
    context = {
        'posts': posts
    }
    return render(request, 'about.html', context=context)


def blog_view(request):
    return render(request, 'blog.html')


def category_view(request):
    posts = Post.objects.filter(is_published=True)
    context = {
        'posts': posts
    }
    return render(request, 'category.html', context=context)


def contact_view(request):
    return render(request, 'contact.html')


def blog_single(request):
    return render(request, 'blog-single.html')
