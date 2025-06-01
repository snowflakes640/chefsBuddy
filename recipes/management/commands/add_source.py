from recipes.models import RecipesDB
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Update source field"

    def handle(self, *args, **options):
        for recipe in RecipesDB.objects.all():
            try:
                recipe.source = "internal"
                recipe.save()
            except:
                print(f"Could not parse instructions for recipe {recipe.id}")
    
        self.stdout.write(self.style.SUCCESS("Successfully updated instructions values!"))