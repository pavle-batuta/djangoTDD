from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import render

def home_page(request):
	# Render the home page.
	# NOTE: templates are expanded from the dictionary
	# Get will return an empty string so that we don't break the webpage when
	# we do not have a valid template expansion!
	return render(request, 'home.html', {
		'new_item_text': request.POST.get('item_text', ''),
	})