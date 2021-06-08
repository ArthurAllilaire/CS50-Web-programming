from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("new-listing", views.new_listing, name="new-listing"),
    path("<int:listing_id>", views.listing, name="listing"),
    path("register", views.register, name="register")
]
