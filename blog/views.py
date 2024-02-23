from django.shortcuts import render
from .models import Post, Category, Tag
from django.core.paginator import Paginator


def base_view(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'layouts/base.html', context=context)


def home_view(request):
    info = request.GET
    cat = info.get('cat')
    page = info.get("page", 1)
    if info.get('cat'):
        posts = Post.objects.filter(is_published=True, category_id=cat)
    else:
        posts = Post.objects.filter(is_published=True)
    post_obj = Paginator(posts, 2)
    # posts = Post.objects.filter(is_published=True)
    categories = Category.objects.all()
    tags = Tag.objects.all()
    context = {
        'posts': post_obj.page(page),
        'categories': categories,
        'tags': tags
    }
    return render(request, 'index.html', context=context)


def about_view(request):
    posts = Post.objects.filter(is_published=True).order_by('-created_at')
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
    posts = Post.objects.filter(is_published=True)
    tags = Tag.objects.all()
    d = {
        'posts': posts,
        'tags': tags
    }
    return render(request, 'blog-single.html', context=d)
