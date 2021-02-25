from django.shortcuts import render

from . import util

from markdown2 import markdown

from random import choice

def index(request):
	return render(request, "encyclopedia/index.html", {
    	"entries": util.list_entries()
	})

def entry_page(request, title=None):
	if not title:
		title = choice(util.list_entries())
	content = markdown(util.get_entry(title))
	return render(request, "encyclopedia/entry.html", {
        "entries": util.list_entries(),
        "content": content,
        "title": title
    })


def add_entry(request):
	if request.method == "POST":
		entry_title = request.POST.get("title")
		entry = request.POST.get("submission")

		if entry_title in util.list_entries():
			return error(request)

		util.save_entry(entry_title, entry)
		return entry_page(request, entry_title)

	return render(request, "encyclopedia/create_new.html", {
		"entries": util.list_entries()
		})

def error(request):
	return render(request, "encyclopedia/error.html")

def search(request):
	query = request.POST.get("q")
	print(query)
	if query in util.list_entries():
		return entry_page(request, query)
	else:
		matches = []
		for entry in util.list_entries():
			if query.lower() in entry.lower():
				matches.append(entry)
		return render(request, "encyclopedia/search.html", {
		"matches": matches,
		"length": len(matches)
	})

def edit(request, title):
	if request.method == "POST":
		content = request.POST.get("edits")
		util.save_entry(title, content)
		return entry_page(request, title)
	return render(request, "encyclopedia/edit.html", {
		"title":title ,
		"fill":util.get_entry(title)
	})