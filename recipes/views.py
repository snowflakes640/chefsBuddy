from django.shortcuts import render

from django.shortcuts import render
from .services import get_external_recipe
from django.http import HttpResponse

def find_recipe(request):
    return render(request, "recipes/searchRecipe.html")



def ext_recipe_view(request):
    queryString = request.GET.get("queryString", "")
    # queryString = "pancake"
    recipeData = get_external_recipe(queryString)

    return render(request, "recipes/extRecipe.html", {"recipeData": recipeData})

# def ext_recipe_view(request):
#     return HttpResponse("Hello")

