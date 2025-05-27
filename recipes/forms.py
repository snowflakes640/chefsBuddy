from django import forms
from .models import RecipesDB

class SaveRecipeForm(forms.ModelForm):
    class Meta:
        model = RecipesDB
        fields = [
            'title',
            'rating',
            'category_path',
            'prep_time',
            'servings',
            'recipe_url',
            'ingredients',
            'instructions'
        ]

        widgets = {
            'ingredients': forms.Textarea(attrs={
                'rows': 3,
                'cols': 50,
                'id': 'ingredients',       # Match your HTML’s id
                'name': 'ingredients'      # Match your HTML’s name
            }),
            'instructions': forms.Textarea(attrs={
                'rows': 10,
                'cols': 50,
                'id': 'instructions',
                'name': 'instructions'
            }),
        }

    # Override form fields to match your HTML names and IDs
    title = forms.CharField(
        label="Name of the recipe",
        required=False,
        widget=forms.TextInput(attrs={
            'id': 'title',
            'name': 'title'
        })
    )

    rating = forms.FloatField(
        label="Rate the recipe",
        required=False,
        widget=forms.NumberInput(attrs={
            'id': 'rating',
            'name': 'rating'
        })
    )

    category_path = forms.ChoiceField(
        label="Select category",
        choices=[
            ("Main Dishes", "Main Dishes"),
            ("Side Dish", "Side Dish"),
            ("Meat and Poultry", "Meat and Poultry"),
            ("BBQ & Grilling", "BBQ & Grilling"),
            ("Seafood", "Seafood"),
            ("Salad", "Salad"),
            ("Soups & stew", "Soups & stew"),
            ("Fruits and Vegetables", "Fruits and Vegetables"),
            ("Appetizers and Snacks", "Appetizers and Snacks"),
            ("Breakfast and Brunch", "Breakfast and Brunch"),
            ("Everyday Cooking", "Everyday Cooking"),
            ("Bread", "Bread"),
            ("Drinks Recipes", "Drinks Recipes"),
            ("Desserts", "Desserts")
        ],
        required=False,
        widget=forms.Select(attrs={
            'id': 'category',
            'name': 'category'
        })
    )

    prep_time = forms.IntegerField(
        label="Estimated preparation time",
        required=False,
        widget=forms.TextInput(attrs={
            'id': 'prepTime',
            'name': 'prepTime'
        })
    )

    servings = forms.IntegerField(
        label="Servings",
        required=False,
        widget=forms.NumberInput(attrs={
            'id': 'servings',
            'name': 'servings'
        })
    )

    recipe_url = forms.URLField(
        label="Recipe URL",
        required=False,
        widget=forms.TextInput(attrs={
            'id': 'recipeURL',
            'name': 'recipeURL'
        })
    )