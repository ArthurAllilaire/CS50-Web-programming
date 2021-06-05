from django.shortcuts import render
from django.http import HttpResponseNotFound

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def article(request, title):
    #Case specific
    article = util.get_entry(title)
    if article == None:
        return HttpResponseNotFound(f"<h1>The page: {title} was not found. (404 Error)</h1>")
    return render(request, "encyclopedia/article.html", {
        "title": title,
        "article": article
    })


