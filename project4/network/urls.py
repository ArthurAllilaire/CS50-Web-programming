
from network.tests import create_post
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create-post", views.create_post, name="create-post"),
    path("all-posts", views.all_posts, name="all-posts"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register")
]
