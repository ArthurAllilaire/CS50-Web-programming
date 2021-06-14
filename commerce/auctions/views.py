from django.contrib.auth import authenticate, login, logout, get_user_model
from django.db import IntegrityError
from django.forms.widgets import TextInput, Textarea
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.forms import ModelForm
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.contrib.auth.decorators import login_required



from .models import *


def index(request):
    return render(request, "auctions/index.html", {
        "listings": Listing.objects.all()
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
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


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
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

class ListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = "__all__"
        widgets = {
            "title": TextInput(),
            "description": Textarea()
        }

@login_required(login_url='/login')
def new_listing(request):
    if request.method == "POST":
        form = ListingForm(request.POST)
        if form.is_valid():
            new_listing = form.save()
            return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/new-listing.html", {
            "listingform": ListingForm()
        })


class BiddingForm(ModelForm):
    class Meta:
        model = Listing
        fields = ["price"]

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]
        widgets = {
            "text": Textarea()
        }

def listing(request, listing_id):
    listing_inst = Listing.objects.get(id=listing_id)
    if request.method == "POST":
        action = request.POST["action"]
        if action == "Close":
            listing_inst.active = False
            listing_inst.save()
        return HttpResponseRedirect(reverse("listing", args=[listing_inst.id]))
            
    #Check if model user is signed in:
    if request.user.is_authenticated:
        #Check if the listing_inst is already in user's watchlist
        try:
            request.user.watchlist.get(id=listing_id)
        #If not there
        except ObjectDoesNotExist:
            watchlist_message = "Add to watchlist"
            action = "add"
        else:
            watchlist_message = "Remove from watchlist"
            action = "remove"
        #Render the listing page
        return render(request, "auctions/listing.html", {
            "listing": listing_inst,
            "watchlist_message": watchlist_message,
            "action": action,
            "bidding_form": BiddingForm(),
            "comment_form": CommentForm(),
            "comments": listing_inst.comments.all()
        })
    else:
        return render(request, "auctions/listing.html", {
            "listing": listing_inst,
            "bidding_form": BiddingForm(),
            "comment_form": CommentForm(),
            "comments": listing_inst.comments.all()
        })  

@login_required(login_url='/login')
def add_to_watch_list(request, listing_id):
    if request.method == 'POST':
        action = request.POST["action"]
        listing = Listing.objects.get(pk=listing_id)
        #If want to add to watchlist
        if action == "add":
            user = request.user
            user.watchlist.add(listing)
            return HttpResponseRedirect(reverse("listing", args=[listing.id]))
        elif action == "remove":
            user = request.user
            user.watchlist.remove(listing)
            return HttpResponseRedirect(reverse("listing", args=[listing.id]))

@login_required(login_url='/login')
def make_bid(request, listing_id):
    if request.method == "POST":
        #Get instance
        listing = Listing.objects.get(pk=listing_id)
        #Create form based on that data and original instance
        form = BiddingForm(request.POST, instance=listing)
        #try to save the from django.conf import settings 
        proposed_list = form.save(commit=False)
        #Check to make sure price is higher than current price
        #Database has not yet had changes to price
        old_listing = Listing.objects.get(pk=listing_id)
        if proposed_list.price > old_listing.price:
            proposed_list.bidder = request.user
            proposed_list.save()
            return HttpResponseRedirect(reverse("listing", args=[listing_id]))
        #If form is not valid
        else:
            return HttpResponse("Bid must be higher than current price.")
        
    else:
        return render(request, "auctions/new-listing.html", {
            "listingform": ListingForm()
        })

@login_required(login_url='/login')
def make_comment(request, listing_id):
    if request.method == "POST":
        listing = Listing.objects.get(pk=listing_id)
        user = request.user
        comment = Comment(listing=listing, user=user)
        form = CommentForm(request.POST, instance=comment)
        form.save()
        return HttpResponseRedirect(reverse("listing", args=[listing_id]))

@login_required(login_url='/login')
def watch_list(request):
    user = request.user
    return render(request, "auctions/watchlist.html",{
        "watchlist": user.watchlist.all()
    })

def categories(request):
    return HttpResponse("Categories")