from django.shortcuts import render,HttpResponse
import requests

def current_datetime(request):
    return HttpResponse()

def index(request):
    return render(request,'Index.html')
