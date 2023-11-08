from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def pranit(request):
    return HttpResponse('<h1><marquee>hii how r u</h1></marquee>')

