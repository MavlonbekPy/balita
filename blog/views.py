from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category, Tag, Comment
from django.core.paginator import Paginator


def base_view(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'layouts/base.html', context=context)


def blog_search_view(request):
    text = request.GET.get('text')
    text = text.replace('+', ' ')
    posts = Post.objects.filter(title__contains=text)


def home_view(request):
    info = request.GET
    page = info.get("page", 1)
    posts = Post.objects.filter(is_published=True)
    post_obj = Paginator(posts, 3)
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
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'posts': posts
    }
    return render(request, 'about.html', context=context)


def blog_view(request):
    categories = Category.objects.all()

    return render(request, 'blog.html', context={'categories': categories})


def category_view(request):
    cate = request.GET.get('category')
    posts = Post.objects.filter(is_published=True, category__name=cate)
    categories = Category.objects.all()
    context = {
        'posts': posts,
        'categories': categories
    }
    return render(request, 'category.html', context=context)


def contact_view(request):
    categories = Category.objects.all()
    return render(request, 'contact.html', context={'categories': categories})


def blog_single(request, pk):
    if request.method == 'POST':
        print(request.POST)
        comment = Comment.objects.create(post_id=pk, message=request.POST['message'], email=request.POST['email'],

                                         name=request.POST['name'])
        comment.save()
        return redirect(f'/blog/{pk}/')

    # posts = Post.objects.filter(is_published=True, pk=pk)
    posts = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post_id=pk)

    categories = Category.objects.all()
    tags = Tag.objects.all()
    d = {
        'posts': posts,
        'tags': tags,
        'categories': categories,
        'comments': comments
    }
    return render(request, 'blog-single.html', context=d)
