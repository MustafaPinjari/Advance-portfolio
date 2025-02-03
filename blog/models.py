from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    
    slug = models.SlugField(unique=True, blank=True)  # SlugField for SEO-friendly URLs
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)  # Automatically generate a slug if not provided
        super(BlogPost, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
