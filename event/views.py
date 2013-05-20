from django.http import HttpResponseRedirect, HttpResponse
from event.models import *
from django.template import Context, loader
from django.shortcuts import render, get_object_or_404, render_to_response
from django.core.urlresolvers import reverse
from django.utils import timezone

def index(request):
	events = Event.objects.filter(start_date__day = timezone.now().day)
	date = timezone.now()
	context = {'events': events, 'date': date}
	return render_to_response("event/index.html", context)

def engine(request):
	if request.method == 'POST': # If the form has been submitted...
		#day = request.POST['day']
		#month = request.POST['month']
		#text = request.POST['form']

		#events = Event.objects.filter(start_date__day = day, start_date__month = month)
		#date = timezone.now()
		#context = {'events': events, 'date': date}
		#return render(request, "event/index.html", context)
		return HttpResponse("Do something")