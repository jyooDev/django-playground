from django.db import models
from date.models import Date
# Create your models here.
class Tweet(Date):
    payload = models.CharField(max_length=180)
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        default = ""
    )

    def __str__(self):
        return f"{self.user}'s tweet #{self.pk}"
