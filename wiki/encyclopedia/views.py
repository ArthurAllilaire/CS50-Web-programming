from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django import forms
from django.urls import reverse

from . import util

class SearchForm(forms.Form):
    q = forms.CharField(
        label="",
        # Adds class search to the form - from: https://treyhunner.com/2014/09/adding-css-classes-to-django-form-fields/, other solution could be used to have classnames only in front end, not backend.
        widget=forms.TextInput(attrs={'class': "search", "placeholder": "Search Encyclopedia"}),
        
    )

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "form": SearchForm()
    })

def article(request, title):
    article = util.get_entry(title)
    if article == None:
        return HttpResponseNotFound(f"<h1>The page: {title} was not found. (404 Error)</h1>")
    return render(request, "encyclopedia/article.html", {
        "title": title,
        "form": SearchForm(),
        "article": article
    })

def search(request):
    # Check if method is POST
    if request.method == "POST":

        # Take in the data the user submitted and save it as form
        form = SearchForm(request.POST)

        # Check if form data is valid (server-side)
        if form.is_valid():

            # Isolate the task from the 'cleaned' version of form data
            title = form.cleaned_data["q"]

            if util.is_title_valid(title):
                # Redirect user to url of article
                return HttpResponseRedirect(title)
            else:
                #Direct user to search template, pass in articles according to regex expression
                entries = util.regex_article_match(title)
                #If no pages found
                if entries == []:
                    title = "Search query doesn't match any pages"
                else:
                    title = "Matching pages"
                return render(request, "encyclopedia/search.html", {
                    "title": title,
                    "entries": entries,
                    "form": form
                })
    else:
        return HttpResponseRedirect(reverse("index"))
            

    #return render(request, "encyclopedia/search.html")


