from django.urls import path
from .views import get_merged_list_API, recipe_details_API, save_myRecipe_API

urlpatterns = [
    path("showList/", get_merged_list_API, name="merged_list_API"),
    path("details/<str:recipe_id>/", recipe_details_API, name="recipe_details_API"),
    path("saveRecipe/", save_myRecipe_API, name="save_myRecipe_API"),
]