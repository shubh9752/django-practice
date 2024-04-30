from django.shortcuts import render, redirect
from .models import *

# Create your views here.

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
        queryset=queryset.filter(name__icontains = (request.GET.get('search')))
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
   
    
