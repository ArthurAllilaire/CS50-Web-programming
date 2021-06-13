from django.test import TestCase
from djmoney.money import Money
from decimal import Decimal

# Create your tests here.
from .models import User, Listing, Comment

def create_test_user(id = ""):
  """
  Creates a user, takes an optional id to differentiate different test users. (id is appended to test_user for username and example{id}@example.com)
  """
  username = f"test_user{id}"
  email = f"example{id}@example.com"
  password = "password1"
  return User.objects.create_user(username, email, password)

def create_listing(user, title, description, price, currency="USD"):
  """
  Args:
    price: str of a number, converted into money instance.
    currency: Default is USD, change if needed.
  """
  return Listing.objects.create(user=user, title=title, description=description, price=Money(Decimal(price), currency))

def create_comment(user, listing, text):
  """
  Creates a comment.
  """
  return Comment.objects.create(user=user, listing=listing, text=text)

class UserModelTests(TestCase):


  def test_watchlist_adds_listings(self):
    user = create_test_user()
    user1 = create_test_user("1")
    listing1 = create_listing(
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
    user = create_test_user()
    pass

class CommentModelTests(TestCase):
  def test_listing_can_access_comments(self):
    user = create_test_user()
    user1 = create_test_user("1")
    listing1 = create_listing(
      user1, "Title1", "description1", "100" 
    )
    comment1 = create_comment(user, listing1, "comment1")
    self.assertQuerysetEqual(listing1.comments.all(), Comment.objects.all())