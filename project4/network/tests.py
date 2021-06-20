from django.test import TestCase, Client
from .models import User, Post
# Create your tests here.

def create_user(id = "", follows=None, followers=None):
  """
  Creates a user, takes an optional id to differentiate different test users. (id is appended to test_user for username and example{id}@example.com)
  Takes optional user query set (or single object) for users the user follows and users who follow the user.

  returns the user that has been created (already saved to the database)
  """
  username = f"test_user{id}"
  email = f"example{id}@example.com"
  password = "password1"
  user = User.objects.create_user(username=username, email=email, password=password)

  if follows:
    user.follows.add(follows)
  
  if followers:
    user.followers.add(followers)

  user.save()
  return user

def create_post(user, text, likes=None):
  """
  Creates a post. returns the created post
  Args:
    user: User object
    text: has to be less than 1000 characters
    likes: User object or query set of users added to likes of post.

  """
  post = Post.objects.create(user=user, text=text)
  if likes:
    post.likes.add(user)
    post.save()  
  return post


class UserModelTests(TestCase):
  def setUp(self):
    """ Creates users and posts """
    user = create_user()
    user1 = create_user("1")
    user2 = create_user("2")

    # Create posts
    post1 = create_post(user1, "post1")
    post2 = create_post(user2, "post2")

  def test_user_add_following(self):
    user = User.objects.get(username="test_user")
    user1 = User.objects.get(username="test_user1")
    user2 = User.objects.get(username="test_user2")
    
    # User follows user1 - add saves automatically
    user.follows.add(user1)

    #user should now have queryset with user1
    self.assertQuerysetEqual(user.follows.all(), User.objects.filter(username="test_user1"))

  def test_user_adds_followers(self):
    user = User.objects.get(username="test_user")
    user1 = User.objects.get(username="test_user1")
    user2 = User.objects.get(username="test_user2")
    
    # User follows user1 - add saves automatically
    user.follows.add(user1)
    user2.follows.add(user1)
    # same as
    user1.followers.add(user, user2)

    #user should now have queryset with user1
    self.assertQuerysetEqual(user1.followers.all(), User.objects.exclude(username="test_user1"), ordered=False)


class PostModelTests(TestCase):  
  def setUp(self):
    """ Creates users and posts """
    user = create_user()
    user1 = create_user("1")
    user2 = create_user("2")

    # Create posts
    post1 = create_post(user1, "post1")
    post2 = create_post(user2, "post2")

  def test_add_post(self):
    """ Testing create_post function """
    print(Post.objects.get(text="post2").date)
    self.assertTrue(Post.objects.all().count() == 2)

  def test_liking_post(self):
    """ Liking post and checking can retrieve user who liked it and number of likes """
    user3 = create_user("3")
    user = User.objects.get(username="test_user")
    user1 = User.objects.get(username="test_user1")
    user2 = User.objects.get(username="test_user2")
    post3 = create_post(user3, "post3")

    post3.likes.add(user, user1, user2)

    self.assertQuerysetEqual(post3.likes.all(), User.objects.exclude(username=user3), ordered=False)

    self.assertQuerysetEqual(user.likedPosts.all(), [post3])



  def test_unliking_post(self):
    user3 = create_user("3")
    user = User.objects.get(username="test_user")
    user1 = User.objects.get(username="test_user1")
    user2 = User.objects.get(username="test_user2")
    post3 = create_post(user3, "post3")

    post3.likes.add(user, user1, user2)
    post3.likes.remove(user)
    self.assertQuerysetEqual(post3.likes.all(), User.objects.exclude(username=user3).exclude(username=user), ordered=False)

  