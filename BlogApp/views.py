from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog, Tag

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

    context = {
        "blog_title": blog_title,
        "blog_content": blog_content,
        "tags": tags
    }

    return render(request, "create_blog.html", context)


def update_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    tags = Tag.objects.all()

    if request.method == "POST":
        blog_title = request.POST.get("blog_title")
        blog_content = request.POST.get("blog_content")
        selected_tags = request.POST.getlist("blog_tags")

        if blog_title:
            blog.title = blog_title
        if blog_content:
            blog.content = blog_content

        blog.tags.clear()
        for tag_id in selected_tags:
            tag = Tag.objects.get(id=tag_id)
            blog.tags.add(tag)

        blog.save()
        return redirect("home")

    context = {
        "blog": blog,
        "tags": tags,
    }

    return render(request, "update_blog.html", context)

def view_blog(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    return render(request, "view_blog.html", {"blog": blog})

def home(request):
    blogs = Blog.objects.all()
    return render(request, "home.html", {"blogs": blogs})
