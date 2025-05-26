import csv
from django.core.management.base import BaseCommand
from recipes.models import RecipesDB

class Command(BaseCommand):
    help = "Import JSON data"

    def handle(self, *args, **options):
        with open (r'H:\workspace\projects\chefsBuddy\recipes\recipes.csv', newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                title = row.get("recipe_name")
                rating = row.get("rating")
                category_path = row.get("cuisine_path")
                prep_time = row.get("total_time	")
                servings = row.get("servings")
                ingredients = row.get("ingredients")
                instructions = row.get("directions")
                recipe_url = row.get("url")

                RecipesDB.objects.create(
                    title = title,
                    rating = rating,
                    category_path = category_path,
                    prep_time = prep_time,
                    servings = servings,
                    ingredients = ingredients,
                    instructions = instructions,
                    recipe_url = recipe_url
                )

        self.stdout.write(self.style.SUCCESS('Successfully imported CSV data!'))




































# import requests
# import string
# from django.core.management.base import BaseCommand
# from recipe.models import RecipesDB

# class Command(BaseCommand):
#     help = "Fetch data from the external API and populate the database"

#     def handle(self, *args, **kwargs):
#         res = string.ascii_lowercase[:26]
#         for i in res:
#             response = requests.get(f"https://www.themealdb.com/api/json/v1/1/search.php?f={i}")
#             if response.status_code == 200:
#                 data = response.json()
#                 meal_list = data.get("meals")
#                 if meal_list:
#                     for meal in meal_list:
#                         RecipesDB.objects.update_or_create(
#                             slug = meal['idMeal'],
#                             title = meal['strMeal'],
#                             category = meal['strCategory'],
#                             region = meal['strArea'],
#                             instructions = meal['strInstructions'],
#                             image_url = meal['strMealThumb']
#                         )
#                     self.stdout.write(self.style.SUCCESS("Successflly populated"))
#             else:
#                 self.stdout.write(self.style.ERROR("Failed to fetch data"))