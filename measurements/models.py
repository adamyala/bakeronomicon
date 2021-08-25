from django.db import models

from django_extensions.db.models import TimeStampedModel, TitleDescriptionModel


class IngredientMeasurement(TimeStampedModel, TitleDescriptionModel):
    recipe_version = models.ForeignKey('recipes.RecipeVersion', on_delete=models.CASCADE)
    ingredient = models.ForeignKey('ingredients.Ingredient', on_delete=models.CASCADE)

    amount = models.IntegerField()

    class Units(models.TextChoices):
        G = 'gram'
        TSP = 'teaspoon'

    unit = models.CharField(max_length=255, choices=Units.choices)
