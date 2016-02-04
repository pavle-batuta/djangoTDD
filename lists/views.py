from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import redirect, render

from lists.models import Item

def home_page(request):
	# Render the home page.
	# NOTE: templates are expanded from the dictionary
	# Get will return an empty string so that we don't break the webpage when
	# we do not have a valid template expansion!
	if request.method == 'POST':
		Item.objects.create(text=request.POST['item_text'])
		return redirect('/lists/the-only-list-in-the-world/')

	return render(request, 'home.html', {'items': Item.objects.all()})

def view_list(request):
	items = Item.objects.all()
	return render(request, 'list.html', {'items': items})