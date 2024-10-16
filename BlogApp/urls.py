from django.urls import path
from . import views

urlpatterns = [
    path("", views.list_blogs, name="list_blogs"),
]