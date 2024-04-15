from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def my_bakery(request):
    return HttpResponse("Hello, Bakery")