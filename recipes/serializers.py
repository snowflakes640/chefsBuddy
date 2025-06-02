from rest_framework import serializers
from .models import RecipesDB

class RecipeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RecipesDB
        fields = ("title", "rating", "category", "prep_time", "servings",
                  "ingredients", "instructions", "source", "recipe_url")