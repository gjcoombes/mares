from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Welcome to the grids index")


def find_grid(request):
    return  HttpResponse("This is the find grid page")