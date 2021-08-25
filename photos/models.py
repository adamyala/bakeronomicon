from django.db import models

from django_extensions.db.models import TimeStampedModel, TitleDescriptionModel


class Photo(TimeStampedModel, TitleDescriptionModel):
    batch = models.ForeignKey('batches.Batch', on_delete=models.CASCADE)

    file = models.FileField()
