'''
For foreign key.
If you need to create a relationship on a model that has not yet been defined, you can use the name of the model, rather than the model object itself:
https://docs.djangoproject.com/en/3.2/ref/models/fields/#django.db.models.ForeignKey


'''
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL

from djmoney.models.fields import MoneyField

class User(AbstractUser):
    watchlist = models.ManyToManyField(
        "Listing", blank=True, related_name="watchers")


class Listing(models.Model):
    # I want to create new listing - one to many relationship between comments and listing - done in comment model
    # one to many relationship for user to listing
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=CASCADE, related_name="owner")
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    price = MoneyField(
        verbose_name="Starting bid in $:",
        max_digits=14, decimal_places=2, default_currency="USD")
    image = models.ImageField(upload_to="uploads/",
                              verbose_name="Product image", blank=True)
    CATEGORY_CHOICES = [
        ("Pets", "Pets"),
        ("Furniture", "Furniture"),
        ("Cars", "Cars"),
        ("Human Parts", "Human Parts"),
        ("Houses", "Houses")
    ]
    category = models.CharField(
        max_length=100, blank=True, choices=CATEGORY_CHOICES)

    def __str__(self):
        return f"{self.title}"


class Comment(models.Model):
    listing = models.ForeignKey(
        Listing, on_delete=CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=CASCADE, related_name="author")


# class Watchlist(models.Model):
#     listing = models.ManyToManyField(
#         Listing,
#         related_name="watch_list",
#         blank=True
#     )
#     user = models.OneToOneField(
#         User,
#         on_delete=CASCADE,
#         related_name="watcher",
#         primary_key=True,
#         unique=True
#     )

#     def __str__(self):
#         return f"{self.user}'s watchlist. Watching: {self.listing}"


class Bid(models.Model):
    listing = models.ForeignKey(
        Listing, on_delete=CASCADE, related_name="bids")
    price = MoneyField(verbose_name="Current price in $:",
                       max_digits=14, decimal_places=2, default_currency="USD")
