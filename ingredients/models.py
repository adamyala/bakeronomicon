from django.db import models

from core.models import BaseModel


class Ingredient(models.Model):
    def __str__(self):
        return (
            str(getattr(self, "dryingredient", ""))
            or str(getattr(self, "fatingredient", ""))
            or str(getattr(self, "wetingredient", ""))
        )


class DryIngredient(BaseModel):
    ingredient = models.OneToOneField(
        "ingredients.Ingredient", on_delete=models.CASCADE
    )


class FatIngredient(BaseModel):
    ingredient = models.OneToOneField(
        "ingredients.Ingredient", on_delete=models.CASCADE
    )

    fat_content = models.IntegerField()
    water_content = models.IntegerField()


class WetIngredient(BaseModel):
    ingredient = models.OneToOneField(
        "ingredients.Ingredient", on_delete=models.CASCADE
    )

    fat_content = models.IntegerField()
    water_content = models.IntegerField()
