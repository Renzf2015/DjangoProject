from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    context = {'boldmessage': "I am bold font from the context"}
    return render(request, 'rango/index.html', context)

def about(request):
    return HttpResponse('<a href="/rango/">Index</a><br/>Rango says here is the about page!')