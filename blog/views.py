from django.shortcuts import render


def home_view(request):
    return render(request, 'index.html')


def about_view(request):
    return render(request, 'about.html')


def blog_view(request):
    return render(request, 'blog.html')


def category_view(request):
    return render(request, 'category.html')


def contact_view(request):
    return render(request, 'contact.html')


def blog_single(request):
    return render(request, 'blog-single.html')
