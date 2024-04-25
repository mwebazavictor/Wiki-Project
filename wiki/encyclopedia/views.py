from django import forms
from django.shortcuts import render

from . import util

class New_entry(forms.Form):
    title = forms.CharField(label="Title")

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
def entry(request, title):
    return render(request, "encyclopedia/entry.html", {"title":title,"entry": util.get_entry(title),})

def search(request):
    query = request.GET.get('q')
    entry(request, title=query)

def new_entry(request):
    if request.method == "POST":
        return True
    return render(request, "encyclopedia/add.html", {"form":New_entry})



def error_message(request):
    return render(request, "encyclopedia/error.html")