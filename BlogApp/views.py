from django.shortcuts import render

def list_blogs(request):
    return render(request, "home.html")
