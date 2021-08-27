from django_extensions.db.models import TimeStampedModel, TitleDescriptionModel


class BaseModel(TimeStampedModel, TitleDescriptionModel):
    def __str__(self):
        return self.title

    class Meta:
        abstract = True
