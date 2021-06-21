from django.test import TestCase, Client
from .models import User, Post
from django.urls.base import reverse

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

def create_num_of_users(num_users):
  """ Takes number of users to create (int) and returns list of test_users which have been created """
  for num in range(num_users):
    if num == 0:
      result = [create_user()]
    else:
      result.append(create_user(str(num)))

  return result

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

  
class PostsViews(TestCase):
  def test_following_posts(self):
    users = create_num_of_users(5)

    user = users[0]
    user1 = users[1]

    # Make all users follow user
    user.followers.add(users[1], users[2], users[3], users[4])

    #Create posts for users
    post1 = create_post(user, "Post1")
    post2 = create_post(user, "Post2")

    #Login user1
    self.client.force_login(user1)

    #Get the web page
    response = self.client.get(reverse("following-posts"))

    #Make sure posts are in the context and in the right order
    self.assertQuerysetEqual(response.context["posts"], Post.objects.all().order_by("-date"))

    #Make sure the text is contained on the page
    self.assertContains(response, "Post1" and "Post2")

    #Add user2 posts
    user2 = users[2]

    #Create posts for user2
    post1 = create_post(user2, "Post3")
    post2 = create_post(user2, "Post4")

    #user1 follows user2
    user1.follows.add(user2)

    #Get the web page
    response = self.client.get(reverse("following-posts"))

    #Make sure posts are in the context and in the right order
    self.assertQuerysetEqual(response.context["posts"], Post.objects.all().order_by("-date"))

    #Make sure the text is contained on the page
    self.assertContains(response, "Post1" and "Post2" and "Post3" and "Post4")

    #Unfollow user from user1
    user1.follows.remove(user)

    #Get the web page
    response = self.client.get(reverse("following-posts"))

    #Make sure posts are in the context and in the right order
    self.assertQuerysetEqual(response.context["posts"], Post.objects.filter(user=user2).order_by("-date"))

    #Make sure the text is contained on the page
    self.assertContains(response, "Post3" and "Post4")