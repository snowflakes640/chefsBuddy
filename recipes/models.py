from django.db import models


class RecipesDB(models.Model):
    title = models.CharField(max_length=100, blank = True, null = True)
    rating = models.FloatField(blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)
    prep_time = models.CharField(max_length=100, blank=True, null=True)
    servings = models.IntegerField(blank=True, null=True)
    ingredients = models.CharField(max_length=2000, blank = True, null = True)
    instructions = models.JSONField(max_length=5000, blank = False, null = True)
    source = models.CharField(max_length=20, default="internal")
    recipe_url = models.CharField( max_length=200, blank = True, null = True)

    def __str__(self):
        return self.title
