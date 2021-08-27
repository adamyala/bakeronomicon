from django.db import models

from core.models import BaseModel


class Photo(BaseModel):
    batch = models.ForeignKey("batches.Batch", on_delete=models.CASCADE)

    file = models.FileField()
