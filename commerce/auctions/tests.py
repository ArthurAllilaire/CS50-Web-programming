from django.test import TestCase
from djmoney.money import Money
from decimal import Decimal

# Create your tests here.
from .models import User, Listing

class UserModelTests(TestCase):

  def create_test_user(self, id = ""):
    """
    Creates a user, takes an optional id to differentiate different test users. (id is appended to test_user for username and example{id}@example.com)
    """
    username = f"test_user{id}"
    email = f"example{id}@example.com"
    password = "password1"
    return User.objects.create_user(username, email, password)
  
  def create_listing(self, user, title, description, price, currency="USD"):
    """
    Args:
      price: str of a number, converted into money instance.
      currency: Default is USD, change if needed.
    """
    return Listing.objects.create(user=user, title=title, description=description, price=Money(Decimal(price), currency))

  def test_watchlist_adds_listings(self):
    user = self.create_test_user()
    user1 = self.create_test_user("1")
    listing1 = self.create_listing(
      user1, "Title1", "description1", "100" 
    )
    #Add listing1 to the watchlist
    user.watchlist.add(listing1)
    #Get all listings being watched
    listings_watched = user.watchlist.all()
    #Ensure they are the same
    self.assertQuerysetEqual(Listing.objects.all(), listings_watched)
    print(listings_watched)

  def test_watchlist_returns_listings(self):
    """
    Tests that watchlist attribute of User returns a Query set of lists that the user is watching.
    """
    user = self.create_test_user()
    pass


