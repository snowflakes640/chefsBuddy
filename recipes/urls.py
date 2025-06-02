from django.urls import path, include
from .views import *



urlpatterns = [
    path("search/", search_recipe, name="search_recipe"),
    path("showList/", get_merged_list, name="view_merged_list"),
    path("details/<str:recipe_id>/", merged_recipe_details, name="merged_recipe_details"),
    path("saveRecipe/", save_myRecipe, name="save_myRecipe"),
    # path("showList/", ext_recipe_list, name="view_ext_recipe_list"),
    # path("myDB/search/", search_recipe, name="search_recipe"),
    # path("myDB/list", int_recipe_list, name="view_int_recipe_list"),
    # path("myDB/details/<int:recipe_id>/", recipe_details, name="recipe_details"),
    # path("mergedDetails/", merged_details, name="view-merged-details")
    
]
