from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("blog/<int:blog_id>", views.view_blog, name="view_blog"),
    path("create_blog/", views.create_blog, name="create_blog"),
    path('update/<int:blog_id>/', views.update_blog, name='update_blog'),
]