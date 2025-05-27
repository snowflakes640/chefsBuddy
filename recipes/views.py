from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import render
from .services import get_external_recipe
from .models import RecipesDB
from .forms import SaveRecipeForm


def find_recipe(request):
    return render(request, "recipes/searchRecipe.html")

def save_myRecipe(request):
    if request.method == "GET":
        form = SaveRecipeForm()
    elif request.method == "POST":
        form = SaveRecipeForm(request.POST)
        if form.is_valid():
            form.save()
            recipe_title = form.cleaned_data.get("title")
            messages.success(request, f"The recipe for '{recipe_title}' has been successfully saved!")
            return redirect("save_myRecipe")
        else:
            messages.error(request, f"Form errors: {form.errors}")
        
    return render(request, "recipes/save_myRecipe.html", {"form":form})

    # elif request.method == "POST":
    #     title = request.POST.get("title")
    #     rating = request.POST.get("rating")
    #     category = request.POST.get("category")
    #     prepTime = request.POST.get("prepTime")
    #     servings = request.POST.get("servings")
    #     recipeURL = request.POST.get("recipeURL")
    #     ingredients = request.POST.get("ingredients")
    #     instructions = request.POST.get("instructions")

    #     try: 
    #         rating = float(rating) if rating else None
    #     except ValueError:
    #         rating = None

    #     try:
    #         servings = int(servings) if servings else None
    #     except ValueError:
    #         servings = None

        

    #     if not instructions:
    #         messages.error(request, "You forgot to put the steps")
    #         return redirect("save_myRecipe")
    #     RecipesDB.objects.update_or_create(
    #         title = title,
    #         rating = rating,
    #         category_path = category,
    #         prep_time = prepTime,
    #         servings = servings,
    #         ingredients = ingredients,
    #         instructions = instructions,
    #         recipe_url = recipeURL
    #     )

    #     messages.success(request, f"The recipe of {title} successfully saved!")
    #     return redirect("save_myRecipe")


def ext_recipe_view(request):
    queryString = request.GET.get("queryString", "")
    # queryString = "pancake"
    recipeData = get_external_recipe(queryString)

    return render(request, "recipes/extRecipe.html", {"recipeData": recipeData})

# def ext_recipe_view(request):
#     return HttpResponse("Hello")

