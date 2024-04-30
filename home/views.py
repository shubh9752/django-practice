from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    peoples=[
        {"name": "John",'age':18},
        {"name": "Johna",'age':19},
        {"name": "Johnb",'age':10},
        {"name": "Johnc",'age':28},
    ]
    return render(request,'home\home.html',context={"peoples":peoples})
def success_page(req):
    return HttpResponse('<h1>this is a success page </h1>')


# Create your views here.
