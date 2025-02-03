import markdown
from django.shortcuts import render, get_object_or_404
from .models import BlogPost

def blog_list(request):
    # Fetch all blog posts ordered by creation date
    posts = BlogPost.objects.all().order_by('-created_at')
    
    # Convert Markdown content to HTML for each post
    for post in posts:
        post.content = markdown.markdown(post.content)

    return render(request, 'blog/blog_list.html', {'posts': posts})

def blog_detail(request, slug):
    # Use the slug to fetch the blog post
    blog_post = get_object_or_404(BlogPost, slug=slug)
    # Convert Markdown content to HTML
    blog_post.content = markdown.markdown(blog_post.content)
    return render(request, 'blog/blog_detail.html', {'blog_post': blog_post})
