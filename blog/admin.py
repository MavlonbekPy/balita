from django.contrib import admin
from blog.models import Post, Category, Tag, Comment, Contact


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'admin_photo', 'created_at', 'is_published')
    search_fields = ('title', 'description')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'post', 'created_at', 'is_published')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'created_at', 'is_solved')


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Contact, ContactAdmin)
