import markdown2
from django import forms
from django.shortcuts import render
from django.http import HttpResponse

from . import util

class New_entry(forms.Form):
    title = forms.CharField()
    content = forms.CharField(widget=forms.Textarea)

class Edit_entry(forms.Form):
    content = forms.CharField(widget=forms.Textarea)

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
def entry(request, title):
    if util.get_entry(title) == None:
        return HttpResponse("ENTRY DOES NOT EXIST")
    return render(request, "encyclopedia/entry.html", {"title":title,"entry": markdown2.markdown(util.get_entry(title)),})

def search(request):
    query = request.GET.get('q')
    entry(request, title=query)

def error_message(request, error):
    return render(request, "encyclopedia/error.html",{"error_message":error})

def edit_page(request,title):
    form = Edit_entry(initial={'content':util.get_entry(title)})
    return render(request, "encyclopedia/edit.html", {"form":form})

def new_entry(request):
    form = New_entry()
    if request.method == "POST":
        form = New_entry(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            if util.get_entry(title) is not None:
                return error_message(request, f"An entry with the title '{title}' already exists.")
            else:
                util.save_entry(title,content)
                return entry(request, title)
    return render(request, "encyclopedia/add.html", {"form": form})



