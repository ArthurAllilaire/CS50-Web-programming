from django.shortcuts import render
from django.http import HttpResponseNotFound
from django import forms

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
        "article": article
    })

def search(request):
    return render(request, "encyclopedia/search.html")


