from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseRedirect, HttpResponse
from django import forms
from django.urls import reverse

import random
import markdown2

from . import util

# Form for layout.html used to search through entries


class SearchForm(forms.Form):
    q = forms.CharField(
        label="",
        # Adds class search to the form - from: https://treyhunner.com/2014/09/adding-css-classes-to-django-form-fields/, other solution could be used to have classnames only in front end, not backend.
        widget=forms.TextInput(
            attrs={'class': "search", "placeholder": "Search Encyclopedia"}),
    )
# Form to create new entries


class EntryForm(forms.Form):
    title = forms.CharField(
        label="Title:",
        widget=forms.TextInput(attrs={"id": "title_input"})
    )
    content = forms.CharField(
        label="Content:",
        widget=forms.Textarea(
            attrs={"rows": 5, "cols": 20, "id": "content_input"})
    )

class EditEntry(forms.Form):
    title = forms.CharField(
        widget=forms.HiddenInput()
    )
    content = forms.CharField(
        label="",
        widget=forms.Textarea(
            attrs={"rows": 5, "cols": 20, "class": "edit_content_input"})
    )


class EditForm(forms.Form):
    title = forms.CharField(
        widget=forms.HiddenInput()
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
        "edit_form": EditForm(initial={"title":title}),
        "article": markdown2.markdown(article)
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
                # Direct user to search template, pass in articles according to regex expression
                entries = util.regex_article_match(title)
                # If no pages found
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


def new(request):
    # Check if method is POST
    if request.method == "POST":

        # Take in the data the user submitted and save it as form
        form = EntryForm(request.POST)

        # Check if form data is valid (server-side)
        if form.is_valid():

            # Isolate the title and content from the 'cleaned' version of form data
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            # If title already exists
            if util.is_title_valid(title):
                return render(request, "encyclopedia/new.html", {
                    "form": SearchForm(),
                    # Keep inputted values
                    "entry_form": EntryForm(
                        initial={"title":title, "content":content}
                    ),
                    "title": f"The title \"{title}\" already exists,please try again."
                })
            else:
                util.save_entry(title, content)
                return HttpResponseRedirect(title)
    else:
        return render(request, "encyclopedia/new.html", {
            "form": SearchForm(),
            "entry_form": EntryForm(),
            "title": "Create a new encyclopedia entry"
        })

def edit(request):
    # Check if method is POST
    if request.method == "POST":

        # Take in the data the user submitted and save it as form
        form = EditForm(request.POST)

        # Check if form data is valid (server-side)
        if form.is_valid():

            # Isolate the title from the 'cleaned' version of form data
            title = form.cleaned_data["title"]

            return render(request, "encyclopedia/edit.html", {
                "form": SearchForm(),
                # Keep content values
                "entry_form": EditEntry(
                    initial={"title": title,"content":util.get_entry(title)}
                ),
                "title": title
            })
    else:
        return HttpResponseRedirect(reverse("index"))

def save_edit(request):
    # Check if method is POST
    if request.method == "POST":

        # Take in the data the user submitted and save it as form
        form = EditEntry(request.POST)

        # Check if form data is valid (server-side)
        if form.is_valid():

            # Isolate the title from the 'cleaned' version of form data
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            util.save_entry(title, content)
            return HttpResponseRedirect(title)
    else:
        return HttpResponseRedirect(reverse("index"))

def random_article(request):
    title = random.choice(util.list_entries())
    return HttpResponseRedirect(title)