from rest_framework import serializers
from .models import RecipesDB

# class RecipeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = RecipesDB
#         fields = ("id", "title", "rating", "category", "prep_time", "servings",
#                   "ingredients", "instructions", "source", "recipe_url")
        
class CustomDataSerializer(serializers.Serializer):
    title = serializers.CharField()
    rating = serializers.FloatField()
    category = serializers.CharField()
    prep_time = serializers.CharField()
    servings = serializers.IntegerField()
    ingredients = serializers.CharField()
    instructions = serializers.JSONField()
    source = serializers.CharField()
    recipe_url = serializers.CharField()

class SaveRecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model  = RecipesDB
        fields = "__all__"