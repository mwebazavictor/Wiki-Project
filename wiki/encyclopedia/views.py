from django import forms
from django.shortcuts import render

from . import util

class New_entry(forms.Form):
    form = forms.CharField()

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
def entry(request, title):
    return render(request, "encyclopedia/entry.html", {"title":title,"entry": util.get_entry(title),})

def search(request):
    query = request.GET.get('q')
    search = util.get_entry(title=query)
    if search is not None:
        return entry(request, title=query)

def new_entry(request):
    return render(request, "/encyclopedia/add.html")
