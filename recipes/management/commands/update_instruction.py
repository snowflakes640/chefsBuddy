import ast
from recipes.models import RecipesDB
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Update instructions field"

    def handle(self, *args, **options):
        for recipe in RecipesDB.objects.all():
            instr = recipe.instructions
            if isinstance(instr, str):
                try:
                    parsed = ast.literal_eval(instr)
                    if isinstance(parsed, list):
                        recipe.instructions = parsed
                        recipe.save()
                except:
                    print(f"Could not parse instructions for recipe {recipe.id}")
    
        self.stdout.write(self.style.SUCCESS("Successfully updated instructions values!"))