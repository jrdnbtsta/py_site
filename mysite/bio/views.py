from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request, 'bio/home.html')

def contact(request):
	return render(request, 'bio/basic.html', {'content' : ['If you would like to contact me', 'jordanbau@gmail.com']})