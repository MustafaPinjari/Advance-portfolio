from django.contrib import admin
from .models import BlogPost
from django.utils.html import format_html

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'image_preview')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('author', 'created_at')
    search_fields = ('title', 'content')

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 50px; height: auto;" />', obj.image.url)
        return "No Image"
    image_preview.short_description = 'Preview'
