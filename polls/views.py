from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    """Creating HttpRespone For index Hello world"""
    return HttpResponse("Hello! you are in index function")