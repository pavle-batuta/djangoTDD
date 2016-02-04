from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import redirect, render

from lists.models import Item, List

def home_page(request):
	# Render the home page.
	# NOTE: templates are expanded from the dictionary
	# Get will return an empty string so that we don't break the webpage when
	# we do not have a valid template expansion!
	return render(request, 'home.html', {'items': Item.objects.all()})

def view_list(request, list_id):
	list_ = List.objects.get(id=list_id)
	return render(request, 'list.html', {'list': list_})

def new_list(request):
	list_ = List.objects.create()
	Item.objects.create(text=request.POST['item_text'], list=list_)
	return redirect('/lists/%d/' % (list_.id,))

def add_item(request, list_id):
	list_ = List.objects.get(id=list_id)
	Item.objects.create(text=request.POST['item_text'], list=list_)
	return redirect('/lists/%d/' % (list_.id,))