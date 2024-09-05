from django.shortcuts import render
from django.http import HttpResponse

def customers(request):
    return HttpResponse("Hello world!")