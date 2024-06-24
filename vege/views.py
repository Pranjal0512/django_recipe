from django.shortcuts import render, redirect
from vege.models import *

# Create your views here.
def recipeadd(request):
    if request.method == "POST":
        recipe_image = request.FILES.get('recipe_image')   
        recipe_name = request.POST.get('recipe_name')   
        recipe_description = request.POST.get('recipe_description')   

        Recipe.objects.create(
            recipe_name=recipe_name,
            recipe_description=recipe_description,
            recipe_image=recipe_image
        ) 
    return render(request,'recipeadd.html')

def recipesview(request):
    queryset = Recipe.objects.all()

    if request.GET.get('search'):
        queryset=queryset.filter(recipe_name__icontains=request.GET.get('search'))
    
        
    context = {'recipes':queryset}
    
    return render(request, 'recipeviews.html', context)



def del_recipe(request,id):
    queryset = Recipe.objects.get(id=id)
    queryset.delete()
    
    return redirect('/recipesview/')

def update_recipe(request,id):
    queryset = Recipe.objects.get(id = id)
    if request.method == "POST":
        recipe_name = request.POST.get('recipe_name')  
        recipe_description = request.POST.get('recipe_description')
        recipe_image = request.FILES.get('recipe_image')   

        
        queryset.recipe_name=recipe_name,
        queryset.recipe_description=recipe_description,
        if recipe_image:
            queryset.recipe_image=recipe_image
        queryset.save()
        
        return redirect('recipesview/')
    
    context = {'recipe':queryset}
    
    return render(request, 'recipeupdate.html', context)

