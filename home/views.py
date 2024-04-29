from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'home\home.html')
def success_page(req):
    return HttpResponse('<h1>this is a success page </h1>')


# Create your views here.
