from django.db import models

from django_extensions.db.models import TimeStampedModel, TitleDescriptionModel


class Recipe(TimeStampedModel, TitleDescriptionModel):
    pass


class RecipeVersion(TimeStampedModel, TitleDescriptionModel):
    recipe = models.ForeignKey('recipes.Recipe', on_delete=models.CASCADE)
