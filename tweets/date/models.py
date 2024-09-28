from django.db import models

# Create your models here.
class Date(models.Model):
    created_at = models.DateTimeField(
        db_comment="creation date and time",
        auto_now_add=True,
        editable=False,
    )
    updated_at = models.DateTimeField(
        db_comment="last update date and time",
        auto_now=True,
        editable=False,
    )

    class Meta:
        abstract = True