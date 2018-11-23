from django.shortcuts import render
from djang.http import HttpResponse

def home(request):
    return HttpResponse(<h1>Blog Home</h1>)
