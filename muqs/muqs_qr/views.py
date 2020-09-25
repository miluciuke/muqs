from django.shortcuts import render
from django.http import HttpResponse
from muqs_qr.models import Riddle

def index(request):
	
	riddle_list = Riddle.objects.order_by("?")[:1]
	context_dict = {'riddles':riddle_list}
	return render(request, 'muqs_qr/index.html', context_dict)
