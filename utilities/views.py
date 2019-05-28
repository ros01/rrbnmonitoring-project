from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render (request, 'utilities/hospitals_lookup.html')

# Create your views here.
