from django.contrib.auth.models import User
from django.db import models
from django.utils.safestring import mark_safe
from ckeditor.fields import RichTextField
from config.basemodel import BaseModel


class Tag(BaseModel):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Category(BaseModel):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_posts(self):
        return self.post_set.filter(is_published=True)


class Post(BaseModel):
    title = models.CharField(max_length=120)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    tag = models.ManyToManyField(Tag, blank=True)
    description = models.TextField(max_length=200)
    image = models.ImageField(upload_to='posts/')

    is_published = models.BooleanField(default=True)

    def admin_photo(self):
        return mark_safe('<img src="{}" width="70" />'.format(self.image.url))

    admin_photo.short_description = 'Image'
    admin_photo.allow_tags = True

    def __str__(self):
        return self.title


class Comment(BaseModel):
    name = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    message = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    is_published = models.BooleanField(default=True)

    def __str__(self):
        return f"name: {self.name} email: {self.email}"


class Contact(BaseModel):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()

    is_solved = models.BooleanField(default=False)

    def __str__(self):
        return self.name
