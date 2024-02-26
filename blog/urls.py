from django.urls import path
from .views import home_view, blog_view, category_view, contact_view, blog_single, about_view, blog_search_view

urlpatterns = [
    path('', home_view),
    path('blog/', blog_view),
    path('category/', category_view),
    path('contact/', contact_view),
    path('about/', about_view),
    path('blog/<int:pk>/', blog_single)
]
