import csv
from recipes.models import RecipesDB
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Update prep_time field from CSV data"

    def handle(self, *args, **options):
        with open(r'H:\workspace\projects\chefsBuddy\recipes\recipes.csv', newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                title = row.get("recipe_name")
                cuisine_path = row.get("cuisine_path").lstrip("/").split("/")
                category = cuisine_path[0]
                # print(f"category = {category}")

                instructions = row.get("directions").strip(" ").split(".")
                # print(instructions[0])

                # Find the recipe by title
                try:
                    recipes = RecipesDB.objects.filter(title=title)
                    for recipe in recipes:
                        recipe.category = category
                        recipe.instructions = instructions
                        recipe.save()
                except RecipesDB.DoesNotExist:
                    self.stdout.write(self.style.WARNING(f"Recipe not found: {title}"))

        self.stdout.write(self.style.SUCCESS("Successfully updated prep_time values!"))