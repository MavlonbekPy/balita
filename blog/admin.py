from django.contrib import admin
from blog.models import Post, Category, Tag


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'admin_photo', 'created_at', 'is_published')
    search_fields = ('title', 'description')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag)
