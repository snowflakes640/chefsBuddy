from django.urls import path, include
from .views import *



urlpatterns = [
    path("find/", find_recipe, name="find_recipe"),
    path("show/", ext_recipe_list, name="view_ext_recipe_list"),
    path("details/<int:recipe_id>/", extRecipe_details, name="extRecipe_details"),
    path("myDB/search/", search_recipe, name="search_recipe"),
    path("myDB/list", int_recipe_list, name="view_int_recipe_list"),
    path("myDB/details/<int:recipe_id>/", recipe_details, name="recipe_details"),
    path("myDB/saveRecipe/", save_myRecipe, name="save_myRecipe"),
    path("mergedList/", merge_both_list, name="view_both_list")
    
]
