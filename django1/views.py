from django.http import HttpResponse

import random

def hello_world(request):
	return HttpResponse("Hello World")

def rand_page(request, max_rand=100):
	msg = "Random number between 0 and {0}: {1}".format(max_rand, random.randrange(0, int(max_rand)))
	return HttpResponse(msg)