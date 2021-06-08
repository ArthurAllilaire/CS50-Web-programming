from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL

from djmoney.models.fields import MoneyField


class User(AbstractUser):
    pass

class Listing(models.Model):
    #I want to create new listing - one ot many relationship between comments and listing - done in comment model
    #one to many relationship for user to listing
    user = models.ForeignKey(User, on_delete=CASCADE, related_name="owner")
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    price = MoneyField(verbose_name="Starting bid in $:", max_digits=14, decimal_places=2, default_currency="USD")
    image = models.ImageField(upload_to="uploads/", verbose_name="Product image", blank=True)
    category = models.CharField(max_length=100, blank=True)

class Comment(models.Model):
    listing = models.ForeignKey(Listing, on_delete=CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=CASCADE, related_name="author")

class Bid(models.Model):
    listing = models.ForeignKey(Listing, on_delete=CASCADE, related_name="bids")
    price = MoneyField(verbose_name="Current price in $:", max_digits=14, decimal_places=2, default_currency="USD")

