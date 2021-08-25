from django.db import models

from django_extensions.db.models import TimeStampedModel, TitleDescriptionModel


class Ingredient(TimeStampedModel, TitleDescriptionModel):
    pass


class DryIngredient(TimeStampedModel, TitleDescriptionModel):
    ingredient = models.OneToOneField('ingredients.Ingredient', on_delete=models.CASCADE)


class FatIngredient(TimeStampedModel, TitleDescriptionModel):
    ingredient = models.OneToOneField('ingredients.Ingredient', on_delete=models.CASCADE)

    fat_content = models.IntegerField()
    water_content = models.IntegerField()


class WetIngredient(TimeStampedModel, TitleDescriptionModel):
    ingredient = models.OneToOneField('ingredients.Ingredient', on_delete=models.CASCADE)

    fat_content = models.IntegerField()
    water_content = models.IntegerField()
