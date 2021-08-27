from django.db import models

from core.models import BaseModel


class Recipe(BaseModel):
    pass


class RecipeVersion(BaseModel):
    recipe = models.ForeignKey("recipes.Recipe", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.recipe} - {self.title}"
