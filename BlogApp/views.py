from django.shortcuts import render

def list_blogs(request):

    blog_title, blog_content = "", ""

    if request.method == "POST":
        blog_title = request.POST.get("blog_title")
        blog_content = request.POST.get("blog_content")
    
    context = {
        "blog_title": blog_title,
        "blog_content": blog_content,
    }

    return render(request, "home.html", context)
