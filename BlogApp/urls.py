from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("blog/<int:blog_id>", views.view_blog, name="view_blog"),
    path("create_blog/", views.create_blog, name="create_blog"),
    path('delete/<int:blog_id>/', views.delete_blog, name='delete_blog'),
    path('update/<int:blog_id>/', views.update_blog, name='update_blog'),
    path('signup_page/', views.signup_page, name="signup_page"),
    path('login_page/', views.login_page, name="login_page"),
    path('logout_page/', views.logout_page, name="logout_page"),
]