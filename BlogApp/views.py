from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog, Tag
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

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

def delete_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    blog.delete()
    return redirect("home")

def view_blog(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    return render(request, "view_blog.html", {"blog": blog})

def home(request):
    blogs = Blog.objects.all()
    return render(request, "home.html", {"blogs": blogs})

def signup_page(request):
    if request.method == 'POST':
        # Get the form data
        first_name = request.POST.get('firstName')
        lastName = request.POST.get('lastName')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        # filter the user from User model
        user = User.objects.filter(username=username)

        if user.exists():
            messages.info(request, f"{username} already taken!")
            return redirect('login_page')
        else:
            user = User.objects.create(
                first_name = first_name,
                last_name = lastName,
                username = username,
                email = email,
                # password can't be set directly, as it would not encrypt it & remain as raw str!
            )
            # Django's set_password method encrypts the password
            user.set_password(password)
            user.save()  # Save the user to the database
            messages.info(request, f"Account created successfully")

    return render(request, 'signup.html')

# Login Logic
def login_page(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.all().filter(username=username).exists():
            validUser = authenticate(username=username, password=password)
            if validUser:
                login(request, validUser)   # Add user to a session
                return redirect("home")
            else:
                messages.info(request, f"Invalid Password, Try Again")
        else:
            messages.info(request, f"username \"{username}\" Not found")

    return render(request, 'login.html')

def logout_page(request):

    logout(request)
    return redirect('home')