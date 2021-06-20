from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.forms.widgets import TextInput, Textarea
from django.shortcuts import render
from django.urls import reverse
from django.forms import ModelForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist, ValidationError


from .models import User, Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["text"]
        widgets = {
            "text": Textarea()
        }


def index(request):
    return render(request, "network/index.html", {
        "post_form": PostForm(),
    })


def all_posts(request):
    return render(request, "network/all-posts.html", {
        "posts": Post.objects.all().order_by("-date"),
    })


@login_required(login_url="/login")
def create_post(request):
    if request.method == "POST":
        user = request.user
        form = PostForm(request.POST, instance=Post(user=user))
        form.save()
        return HttpResponseRedirect(reverse("index"))

@login_required(login_url="/login")
def follow(request, user_id):
    """ Takes in the user_id of person to be followed or unfollowed and adds authenticated user to follow list """
    if request.method == "POST":
        pass
    # I AM HERE


def user_profile(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except ObjectDoesNotExist:
        return HttpResponseRedirect(reverse("index"))

    #Get all the posts of the user
    posts = user.posts.all().order_by("-date")

    #Check if the authenticated user is different to the current user
    if request.user and request.user != user:
        #Find out if the authenticated user follows the profile user
        try:
            request.user.follows.get(user_id=user.id)
        #If you don't follow 
        except ObjectDoesNotExist:
            action = "Follow"
        else:
            action = "Unfollow"
    else:
        action = False


    return render(request, "network/user-profile.html", {
        "profile-user": user,
        "posts": posts,
        "action": action,
    })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")
