from django.db import models

from core.models import BaseModel


class Batch(BaseModel):
    recipe_version = models.ForeignKey(
        "recipes.RecipeVersion", on_delete=models.CASCADE
    )

    mixing_notes = models.TextField()

    room_temperature = models.IntegerField()
    flour_temperature = models.IntegerField()
    liquid_temperature = models.IntegerField()
    total_first_speed_mixing_time = models.DurationField()
    total_second_speed_mixing_time = models.DurationField()
    temperature_before_fermentation = models.IntegerField()

    fermentation_time = models.DurationField()
    temperature_after_fermentation = models.IntegerField()
    first_fermentation_volume_increase = models.IntegerField()

    def __str__(self):
        return f"{self.recipe_version} - {self.title}"
