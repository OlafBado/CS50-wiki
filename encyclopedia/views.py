from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django import forms
from django.http import HttpResponseRedirect
import random
from django.contrib import messages



from . import util

class NewSearchForm(forms.Form):
    search = forms.CharField(label="Search")

class NewPageForm(forms.Form):
    title = forms.CharField(label="Title")
    content = forms.CharField(widget=forms.Textarea(attrs={'style':'width:1000px; height:300px'}))

class EditForm(forms.Form):
    new_content = forms.CharField(widget=forms.Textarea(attrs={'style':'width:1000px; height:300px'}))

def edit_page(request, title):

    if request.method == "POST":
        form = EditForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data["new_content"]
            util.save_entry(title, content)
            return HttpResponseRedirect(f'/wiki/{ title }')

    initial_data = {
        "new_content": util.get_entry(title)
    }                 
    return render(request, "encyclopedia/editpage.html", {
        "title": title,
        "content": util.get_entry(title),
        "edit_form": EditForm(initial = initial_data),
        "form": NewSearchForm()
    })

def new_page(request):
        
    if request.method == "POST":
        form = NewPageForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            if title in util.list_entries():
                messages.error(request, f"Title {title} already exists!")
                return render(request, "encyclopedia/new_page.html", {
                    "new_page_form": form,
                    "form": NewSearchForm()
                    })
            else:
                util.save_entry(title, content)
                return HttpResponseRedirect(f'/wiki/{ title }')
    return render(request, "encyclopedia/new_page.html", {
        "new_page_form": NewPageForm(),
        "form": NewSearchForm()
    })


def index(request):
    if request.method == "POST":
        form = NewSearchForm(request.POST)
        if form.is_valid():
            search = form.cleaned_data["search"]
            if search in util.list_entries():
                return HttpResponseRedirect(f'/wiki/{ search }')
            else:
                new_list = [string for string in util.list_entries() if search in string]
                return render(request, "encyclopedia/search.html", {
                    "entries": new_list,
                    "search": search,
                    "form": NewSearchForm()
                })

    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "form": NewSearchForm(),
    })

def entries(request, title):
    if title in util.list_entries():
        return render(request, "encyclopedia/entry.html", {
            "content": util.get_entry(title),
            "title": title,
            "form": NewSearchForm()
        })
    else:
        return HttpResponseNotFound()

def search(request):
    return render(request, "encyclopedia/search.html")

def random_page(request):
    list = util.list_entries()
    title = random.choice(list)
    return HttpResponseRedirect(f"/wiki/{ title }")



