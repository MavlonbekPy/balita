from django.urls import path
from .views import home_view, blog_view, category_view, contact_view, blog_single, about_view, blog_search_view

urlpatterns = [
    path('', home_view, name='home'),
    path('blog/', blog_view, name='blog'),
    path('category/', category_view, name='category'),
    path('contact/', contact_view, name='contact'),
    path('about/', about_view, name='about'),
    path('blog/<int:pk>/', blog_single, name='blog-single'),
    path('blog_search/', blog_search_view, name="blog_search")
]
