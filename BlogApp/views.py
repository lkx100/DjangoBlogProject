from django.shortcuts import render
from .models import Blog, Tag
from django.contrib import messages

def create_blog(request):

    blog_title, blog_content = "", ""
    tags = Tag.objects.all()

    if request.method == "POST":
        blog_title = request.POST.get("blog_title")
        blog_content = request.POST.get("blog_content")
        selected_tags = request.POST.getlist("blog_tags")

        blog = Blog(title=blog_title, content=blog_content)
        blog.save()

        for tag_id in selected_tags:
            tag = Tag.objects.get(id=tag_id)
            blog.tags.add(tag)
        
        messages.success(request, "Blog Created Successfully")

    context = {
        "blog_title": blog_title,
        "blog_content": blog_content,
        "tags": tags
    }

    return render(request, "create_blog.html", context)

def view_blog(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    return render(request, "view_blog.html", {"blog": blog})

def home(request):
    blogs = Blog.objects.all()
    return render(request, "home.html", {"blogs": blogs})
