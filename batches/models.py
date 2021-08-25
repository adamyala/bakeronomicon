from django.db import models

from django_extensions.db.models import TimeStampedModel, TitleDescriptionModel


class Batch(TimeStampedModel, TitleDescriptionModel):
    recipe_version = models.ForeignKey('recipes.RecipeVersion', on_delete=models.CASCADE)

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
