from django.db import models

from core.models import BaseModel


class IngredientMeasurement(models.Model):
    recipe_version = models.ForeignKey(
        "recipes.RecipeVersion", on_delete=models.CASCADE
    )
    ingredient = models.ForeignKey("ingredients.Ingredient", on_delete=models.CASCADE)

    amount = models.IntegerField()

    class Units(models.TextChoices):
        G = "gram"
        TSP = "teaspoon"

    unit = models.CharField(max_length=255, choices=Units.choices)

    def __str__(self):
        return f"{self.amount} {self.unit} of {self.ingredient}"
