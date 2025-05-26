from django.urls import path, include
from .views import *



urlpatterns = [
    path("show/", ext_recipe_view, name="view-extRecipe"),
    path("find/", find_recipe, name="find-recipe")
]
