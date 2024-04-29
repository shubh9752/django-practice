from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>this is my home </h1>')
def success_page(req):
    return HttpResponse('<h1>this is a success page </h1>')


# Create your views here.
