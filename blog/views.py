from django.db.models import Count
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category, Tag, Comment, Contact
from django.core.paginator import Paginator
import requests


def base_view(request):
    posts = Post.objects.filter(is_published=True).annotate(num_comments=Count('comment')).order_by('-created_at')
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'posts': posts
    }
    return render(request, 'layouts/base.html', context=context)


def blog_search_view(request):
    query = request.GET.get('text')
    if query:
        query = query.replace('+', ' ')
        posts = Post.objects.filter(title__icontains=query)
    else:
        posts = Post.objects.all()

    popular_posts = Post.objects.filter(is_published=True).annotate(num_comments=Count('comment')).order_by(
        '-num_comments')[:3]
    recent_posts = Post.objects.filter(is_published=True).annotate(num_comments=Count('comment')).order_by(
        '-created_at')[:3]

    return render(request, 'index.html', {'posts': posts, 'popular_posts': popular_posts, 'recent_posts': recent_posts})


# def blog_search_view(request):
#     text = request.GET.get('text')
#     text = text.replace('+', ' ')
#     posts = Post.objects.filter(title__contains=text)


def home_view(request):
    info = request.GET
    page = info.get("page", 1)
    posts = Post.objects.filter(is_published=True).annotate(num_comments=Count('comment')).order_by('-created_at')
    post_obj = Paginator(posts, 4)
    categories = Category.objects.all()
    count = categories.count()
    tags = Tag.objects.all()
    popular_posts = Post.objects.filter(is_published=True).annotate(num_comments=Count('comment')).order_by(
        '-num_comments')[:3]
    recent_posts = Post.objects.filter(is_published=True).annotate(num_comments=Count('comment')).order_by(
        '-created_at')[:3]

    context = {
        'posts': post_obj.page(page),
        'categories': categories,
        'tags': tags,
        'popular_posts': popular_posts,
        'count': count,
        'recent_posts': recent_posts
    }
    return render(request, 'index.html', context=context)


def category_view(request):
    info = request.GET
    page = info.get("page", 1)
    cate = request.GET.get('category')
    posts = Post.objects.filter(is_published=True, category__name=cate).annotate(
        num_comments=Count('comment')).order_by('-created_at')
    popular_posts = Post.objects.filter(is_published=True).annotate(num_comments=Count('comment')).order_by(
        '-num_comments')[:3]
    recent_posts = Post.objects.filter(is_published=True).annotate(num_comments=Count('comment')).order_by(
        '-created_at')[:3]
    posts_obj = Paginator(posts, 2)
    tags = Tag.objects.all()
    categories = Category.objects.all()
    context = {
        'posts': posts_obj.page(page),
        'categories': categories,
        'tag': tags,
        'recent_posts': recent_posts,
        'popular_posts': popular_posts
    }
    return render(request, 'category.html', context=context)


def about_view(request):
    tags = Tag.objects.all()
    posts = Post.objects.filter(is_published=True).annotate(num_comments=Count('comment')).order_by('-created_at')
    popular_posts = Post.objects.filter(is_published=True).annotate(num_comments=Count('comment')).order_by(
        '-num_comments')[:3]
    recent_posts = Post.objects.filter(is_published=True).annotate(num_comments=Count('comment')).order_by(
        '-created_at')[:4]
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'posts': posts,
        'tags': tags,
        'popular_posts': popular_posts,
        'recent_posts': recent_posts
    }
    return render(request, 'about.html', context=context)


def blog_view(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'blog.html', context=context)


def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        contact = Contact.objects.create(name=name, email=email, phone=phone, message=message)

        token = "6749312297:AAHVOEH5pugcBZZt3aRaXwf8YgflvnQO6vg"
        chat_id = "5210463524"
        message_text = f"From Balita:\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
        telegram_url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message_text}"
        requests.get(telegram_url)

        return redirect('/contact/')

    posts = Post.objects.filter(is_published=True).annotate(num_comments=Count('comment'))
    popular_posts = Post.objects.filter(is_published=True).annotate(num_comments=Count('comment')).order_by(
        '-num_comments')[:3]
    categories = Category.objects.all()
    context = {
        'posts': posts,
        'categories': categories,
        'popular_posts': popular_posts
    }

    return render(request, 'contact.html', context=context)


def blog_single(request, pk):
    if request.method == 'POST':
        print(request.POST)
        comment = Comment.objects.create(post_id=pk, message=request.POST['message'], email=request.POST['email'],

                                         name=request.POST['name'])
        comment.save()
        return redirect(f'/blog/{pk}/')

    posts = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post_id=pk)
    popular_posts = Post.objects.filter(is_published=True).annotate(num_comments=Count('comment')).order_by(
        '-num_comments')[:3]
    recent_posts = Post.objects.filter(is_published=True).annotate(num_comments=Count('comment')).order_by(
        '-created_at')[:3]

    categories = Category.objects.all()
    tags = Tag.objects.all()
    d = {
        'posts': posts,
        'tags': tags,
        'categories': categories,
        'comments': comments,
        'popular_posts': popular_posts,
        'contact': 'active',
        'recent_posts': recent_posts
    }
    return render(request, 'blog-single.html', context=d)
