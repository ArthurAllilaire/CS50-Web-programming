
from network.tests import create_post
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create-post", views.create_post, name="create-post"),
    path("edit-post", views.edit_post, name="edit-post"),
    path("all-posts", views.all_posts, name="all-posts"),
    # Can add optional page argument to get a specific page
    path("all-posts/<int:page_num>", views.all_posts, name="all-posts"),
    path("following-posts", views.following_posts, name="following-posts"),
    path("following-posts/<int:page_num>",
         views.following_posts, name="following-posts"),
    path("user-profile/<int:user_id>", views.user_profile, name="user-profile"),
    path("user-profile/<int:user_id>/<int:page_num>",
         views.user_profile, name="user-profile"),
    path("follow/<int:user_id>", views.follow, name="follow"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register")
]
