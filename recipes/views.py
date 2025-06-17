from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from .services import get_APIrecipe_details, get_APIrecipe_list
from .models import RecipesDB
from .forms import SaveRecipeForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import CustomDataSerializer, SaveRecipeSerializer


@api_view(["GET"])
def get_merged_list_API(request):
    q = request.GET.get("q", "")
    tags = request.GET.get("tags", "")
    size = request.GET.get("size", "10")
    params = {
        "q": q,
        "tags": tags,
        "size": size,
        "from": "0"
    }
    response_data = get_APIrecipe_list(params)
    recipeData = response_data.get("results", [])
    cleaned_extAPI_data = get_clean_extAPI_data(recipeData)

    #handling internal db
    db_response_data = RecipesDB.objects.filter(title__icontains = q)[:10]
    dbRecipe_data = list(db_response_data)
    
    merged_list =  dbRecipe_data + cleaned_extAPI_data
    serializer = CustomDataSerializer(merged_list, many=True)

    return Response(serializer.data)

@api_view(["GET"])
def recipe_details_API(request, recipe_id):  
    id = recipe_id.split(":")
    if id[0] == "recipe":
        params = {
            "id": int(id[1])
        }
        response_data = get_APIrecipe_details(params)
        recipeData_det = [response_data]
        recipe_details = get_clean_extAPI_data(recipeData_det)
    else:
        recipe_details = [get_object_or_404(RecipesDB, id=recipe_id)]

    serializer = CustomDataSerializer(recipe_details, many=True)   
    return Response(serializer.data)

@api_view(["GET", "POST"])
def save_myRecipe_API(request):

    if request.method == "GET":
        #providing an empty serializer like an empty form
        serializer = SaveRecipeSerializer()
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = SaveRecipeSerializer(data = request.data)
        if serializer.is_valid():
            recipe = serializer.save()
            # recipe_title = serializer.get("title")
            recipe_title = recipe.title
            return Response(
                {
                    "message": f"The recipe for '{recipe_title}' has been successfully saved!",
                    "recipe": SaveRecipeSerializer(recipe).data
                }, status=status.HTTP_201_CREATED
            )
            
        else:
            print(serializer.errors)
            return Response(
                {
                    "message": "Error in submission",
                    "errors": serializer.errors
                }, status=status.HTTP_400_BAD_REQUEST
            )
        


## search for recipe
def search_recipe(request):
    return render(request, "recipes/searchAPI.html")

#clean API response into myDB schema
def get_clean_extAPI_data(recipeData):
    cleaned_recipeData = []

    try:
        for recipe in recipeData:
            new_recipeObject = {}

            #title
            slug = recipe["slug"]
            title = slug.replace("-", " ")
            new_recipeObject["title"] = title

            #id
            canonical_id = recipe["canonical_id"]
            numeric_id = None
            if canonical_id and ":" in canonical_id:
                try:
                    numeric_id = canonical_id.split(":")[1]
                except IndexError:
                    print(f"Warning: canonical_id '{canonical_id}' unexpected format, cannot split.")
                    numeric_id = None    
            new_recipeObject["id"] = canonical_id
            new_recipeObject["num_id"] = numeric_id

            #rating
            rating_dec = recipe["user_ratings"]["score"]
            rating = round(rating_dec*5, 2)
            new_recipeObject["rating"] = rating

            #category
            tag_list = []
            for object in recipe["tags"]:
                tag = object["root_tag_type"]
                if tag not in tag_list: tag_list.append(tag)
            new_recipeObject["category"] = tag_list

            #prep_time
            time_minutes = recipe["total_time_minutes"]
            hrs = time_minutes // 60
            mins = time_minutes % 60
            new_recipeObject["prep_time"] = f"{hrs} hrs {mins} mins"

            #servings
            new_recipeObject["servings"] = recipe["num_servings"]

            #ingredients
            ingredient_list = []
            ingredObj = recipe["sections"][0]
            for item in ingredObj["components"]:
                ingredient = item["raw_text"]
                ingredient_list.append(ingredient)
            new_recipeObject["ingredients"] = ingredient_list

            #instructions
            instruction_list = []
            for item in recipe["instructions"]:
                instruct = item["display_text"]
                instruction_list.append(instruct)
            new_recipeObject["instructions"] = instruction_list

            #recipe_URL
            new_recipeObject["recipe_url"] = recipe["original_video_url"]

            #thumbnail image
            new_recipeObject["thumbnail"] = recipe["thumbnail_url"]

            #add source
            new_recipeObject["source"] = "external"

            cleaned_recipeData.append(new_recipeObject)

    except ValueError:
        print(f"Warning: No recipe found")
        cleaned_recipeDatad = None 

    return cleaned_recipeData

#get search result from both internal and external db
def get_merged_list(request):
    #handling ext API
    q = request.GET.get("q", "")
    tags = request.GET.get("tags", "")
    size = request.GET.get("size", "10")
    params = {
        "q": q,
        "tags": tags,
        "size": size,
        "from": "0"
    }
    response_data = get_APIrecipe_list(params)
    recipeData = response_data.get("results", [])
    cleaned_extAPI_data = get_clean_extAPI_data(recipeData)

    #handling internal db
    db_response_data = RecipesDB.objects.filter(title__icontains = q)[:10]
    dbRecipe_data = list(db_response_data)

    #merging list
    # merged_list = [*cleaned_extAPI_data, *dbRecipe_data]
    merged_list =  dbRecipe_data + cleaned_extAPI_data
    # context = {
    #     "cleaned_extAPI_data": cleaned_extAPI_data,
    #     "dbRecipe_data": dbRecipe_data
    # }

    # print(recipeData[0]["instructions"][0]["display_text"])
    return render(request, "recipes/mergedList.html", {"recipe_list": merged_list})

#get details of the clicked recipe
def merged_recipe_details(request, recipe_id):  
    id = recipe_id.split(":")
    if id[0] == "recipe":
        params = {
            "id": int(id[1])
        }
        response_data = get_APIrecipe_details(params)
        recipeData_det = [response_data]
        recipe_details = get_clean_extAPI_data(recipeData_det)
    
    else:
        recipe_details = [get_object_or_404(RecipesDB, id=recipe_id)]
    return render(request, "recipes/recipe_details.html", {"recipeDetail": recipe_details})

#save recipe from user
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




# def ext_recipe_list(request):
#     # querystring = {"from":"0","size":"20","tags":"under_30_minutes"}
#     q = request.GET.get("q", "")
#     tags = request.GET.get("tags", "")
#     size = request.GET.get("size", "20")
#     params = {
#         "q": q,
#         "tags": tags,
#         "size": size,
#         "from": "0"
#     }
#     response_data = get_APIrecipe_list(params)
#     recipeData = response_data.get("results", [])
#     for recipe in recipeData:
#         slug = recipe["slug"]
#         title = slug.replace("-", " ")
#         recipe["title"] = title

#         canonical_id_full = recipe["canonical_id"]
#         numeric_id = None

#         if canonical_id_full and ":" in canonical_id_full:
#             try:
#                 numeric_id = canonical_id_full.split(":")[1]
#             except IndexError:
#                 print(f"Warning: canonical_id '{canonical_id_full}' unexpected format, cannot split.")
#                 numeric_id = None # Or handle appropriately
        
#         recipe["numeric_id"] = numeric_id
#     # print(recipeData[0]["instructions"][0]["display_text"])
#     return render(request, "recipes/extRecipeList.html", {"recipeData": recipeData})


## Internal DB
# def search_recipe(request):
#     return render(request, "recipes/searchRecipe.html")

# def int_recipe_list(request):
#     queryString = request.GET.get("queryString", "")
#     recipe_list = RecipesDB.objects.filter(title__icontains=queryString)

#     return render(request, "recipes/intRecipe.html", {"recipeData": recipe_list})

# def recipe_details(request, recipe_id):
#     recipe = get_object_or_404(RecipesDB, id=recipe_id)
#     # instructions = ast.literal_eval(recipe.instructions)
#     instructions = ast.literal_eval(recipe.instructions)

#     return render(request, "recipes/recipe_details.html", {"recipe": recipe,
#                                                            "instructions": instructions})









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

