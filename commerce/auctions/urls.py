from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("new-listing", views.new_listing, name="new-listing"),
    path("<int:listing_id>", views.listing, name="listing"),
    path("register", views.register, name="register"),
    path("watchlist/<int:listing_id>", views.add_to_watch_list, name="add-to-watchlist"),
    path("watchlist", views.watch_list, name="user-watchlist"),
    path("categories", views.categories, name="categories"),
    path("make-bid/<int:listing_id>", views.make_bid, name="make-bid"),
    path("make-comment/<int:listing_id>", views.make_comment, name="make-comment")
]
