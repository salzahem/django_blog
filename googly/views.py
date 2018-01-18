from django.shortcuts import render
from django.http import JsonResponse
import requests

from django.shortcuts import render
from django.http import JsonResponse
import requests

def place_search(request):
	key = "AIzaSyAe2iff0HUS8qaCkA6EK18bX9jdPgeVuOE"
	search = "Starbucks"
	url = "https://maps.googleapis.com/maps/api/place/textsearch/json?key=%s&query=%s&region=kw"%(key, search)
	

	next_page_token = request.GET.get('next_page')
	if next_page_token:
		url += "&pagetoken=%s"%(next_page_token)

	response = requests.get(url).json()
	
	context = {
	"response": response
	}

	return render(request, 'place_search.html', context)


def place_detail(request):
	key = "AIzaSyAe2iff0HUS8qaCkA6EK18bX9jdPgeVuOE"
	
	place_id = request.GET.get('place_id')

	url = "https://maps.googleapis.com/maps/api/place/details/json?key=%s&placeid=%s"% (key,place_id)

	name_page_token = request.GET.get('name_page')
	if name_page_token:
		url += "&pagetoken=%s"%(name_page_token)

	response = requests.get(url).json()
	
	context = {
	"response": response
	}

	return render(request, 'place_detail.html', context)
	#return JsonResponse(response, safe= False)

