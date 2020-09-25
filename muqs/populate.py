import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'muqs.settings')

import django
django.setup()
from muqs_qr.models import Riddle

def populate():
		 
	riddles = [
		{"title":"1","body":"What question can you never answer yes to?","answer":"asleep?"},
		{"title":"2","body":"What can you break, even if you never pick it up or touch it?","answer":"promise"},
		{"title":"3","body":"I  shave every day, but my beard stays the same. What am I?","answer":"barber"}]
			
	for riddle in riddles:
		add_riddle(riddle["title"], riddle["body"], riddle["answer"])
			
def add_riddle(title, body, answer):
	r = Riddle.objects.get_or_create(title=title)[0]
	r.body=body
	r.answer=answer
	r.save()
	return r
	
if __name__ =='__main__':
	print("populating")
	populate()