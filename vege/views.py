from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/login/")
def recipes(request):
    if request.method=="POST":
        data=request.POST
        recipe_name=data.get('name')
        recipe_desc=data.get('desc')
        recipe_img=request.FILES.get('img')
        
        Recipe.objects.create(name=recipe_name, desc=recipe_desc, img=recipe_img)
        print("data added")
        
        return redirect('/vege/')
    
    queryset=Recipe.objects.all()
    
    if request.GET.get('search'):
        queryset=queryset.filter(name__icontains = (request.GET.get('search'))) #__icontains is a django keyword which checks or works like includes
    context={"recipes":queryset}
        
    
    return render(request,'recipe.html',context )

def update_recipe(req,id):
    queryset=Recipe.objects.get(id=id)
    if req.method=="POST":
        data=req.POST
        recipe_name=data.get('name')
        recipe_desc=data.get('desc')
        recipe_img=req.FILES.get('img')
        
        queryset.name=recipe_name
        queryset.desc=recipe_desc
        if recipe_img:
            queryset.img=recipe_img
        queryset.save()
        print("data updated")
        
        return redirect('/vege/')
    
    context={"recipe":queryset}
    return render(req,'update_recipe.html',context)

def delete_recipe(req,id):
    queryset=Recipe.objects.get(id=id)
    queryset.delete()
    return redirect('/vege/')
   
    
def login_page(req):
    if req.method == 'POST':
        username=req.POST.get('username')
        password=req.POST.get('password')
        
        if not User.objects.filter(username=username).exists():
            messages.error(req,'''user doesn't exist''')
            return redirect('/login/')
            # user=User.objects.get(username=username)
            # if user.check_password(password):
            #     return redirect('/vege/')
            # else:
            #     messages.info(req,'invalid password')
            #     return redirect('/login/')
        user = authenticate(username=username,password=password)
        
        if user is None:
            messages.error(req,'''incorrect password''')
            return redirect('/login/')
        else:
            login(req,user)
            return redirect('/vege/')
            
    return render(req,'login.html')

def logout_page(req):
    logout(req)
    return redirect('/login/')

def register(req):
    if req.method == 'POST':
        first_name=req.POST.get('fname')
        last_name=req.POST.get('lname')
        username=req.POST.get('username')
        password=req.POST.get('password')
        
        user = User.objects.filter(username=username)
        
        if user.exists():
            messages.info(req,'username already exists')
            return redirect('/register/')
        
        user = User.objects.create(
            first_name=first_name,
            last_name=last_name ,
            username=username,         
        )
        user.set_password(password) #to ncript password
        user.save()
        messages.info(req,'registered successfuly')
        return redirect('/register/')
    
    return render(req,'register.html')