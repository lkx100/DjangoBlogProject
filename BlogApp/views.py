from django.shortcuts import render
from .models import Blog
from django.contrib import messages

def create_blog(request):

    blog_title, blog_content = "", ""

    if request.method == "POST":
        blog_title = request.POST.get("blog_title")
        blog_content = request.POST.get("blog_content")

        blog = Blog(title=blog_title, content=blog_content)
        blog.save()
        messages.success(request, "Blog Created Successfully")
    
    context = {
        "blog_title": blog_title,
        "blog_content": blog_content,
    }

    return render(request, "create_blog.html", context)

def view_blog(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    return render(request, "view_blog.html", {"blog": blog})

def home(request):
    blogs = Blog.objects.all()
    return render(request, "home.html", {"blogs": blogs})
