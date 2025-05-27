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
                prep_time = row.get("total_time\t")  # or adjust as needed

                # Find the recipe by title
                try:
                    recipes = RecipesDB.objects.filter(title=title)
                    for recipe in recipes:
                        recipe.prep_time = prep_time
                        recipe.save()
                    self.stdout.write(self.style.SUCCESS(f"Updated prep_time for {title}"))
                except RecipesDB.DoesNotExist:
                    self.stdout.write(self.style.WARNING(f"Recipe not found: {title}"))

        self.stdout.write(self.style.SUCCESS("Successfully updated prep_time values!"))