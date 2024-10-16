from django.shortcuts import render

def list_blogs(request):

    title, content = "", ""

    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
    
    context = {
        "title": title,
        "content": content,
    }

    return render(request, "home.html", context)
