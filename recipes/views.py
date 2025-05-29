from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from .services import get_APIrecipe_details, get_APIrecipe_list
from .models import RecipesDB
from .forms import SaveRecipeForm


## External API
def find_recipe(request):
    return render(request, "recipes/searchAPI.html")

def ext_recipe_list(request):
    # querystring = {"from":"0","size":"20","tags":"under_30_minutes"}
    q = request.GET.get("q", "")
    tags = request.GET.get("tags", "")
    size = request.GET.get("size", "20")
    params = {
        "q": q,
        "tags": tags,
        "size": size,
        "from": "0"
    }
    response_data = get_APIrecipe_list(params)
    recipeData = response_data.get("results", [])
    for recipe in recipeData:
        slug = recipe["slug"]
        title = slug.replace("-", " ")
        recipe["title"] = title

        canonical_id_full = recipe["canonical_id"]
        numeric_id = None

        if canonical_id_full and ":" in canonical_id_full:
            try:
                numeric_id = canonical_id_full.split(":")[1]
            except IndexError:
                print(f"Warning: canonical_id '{canonical_id_full}' unexpected format, cannot split.")
                numeric_id = None # Or handle appropriately
        
        recipe["numeric_id"] = numeric_id


    # print(recipeData[0]["instructions"][0]["display_text"])
    return render(request, "recipes/extRecipeList.html", {"recipeData": recipeData})

def extRecipe_details(request, recipe_id):
    
    params = {
        "id": recipe_id
    }
    response_data = get_APIrecipe_details(params)
    slug = response_data["slug"]
    title = slug.replace("-", " ")
    response_data["title"] = title

    return render(request, "recipes/extRrecipe_details.html", {"recipe": response_data})

## Internal DB
def search_recipe(request):
    return render(request, "recipes/searchRecipe.html")

def int_recipe_list(request):
    queryString = request.GET.get("queryString", "")
    recipe_list = RecipesDB.objects.filter(title__icontains=queryString)

    return render(request, "recipes/intRecipe.html", {"recipeData": recipe_list})

def recipe_details(request, recipe_id):
    recipe = get_object_or_404(RecipesDB, id=recipe_id)

    return render(request, "recipes/recipe_details.html", {"recipe": recipe})



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




# def ext_recipe_view(request):
#     return HttpResponse("Hello")

