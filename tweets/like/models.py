from django.db import models
from date.models import Date

# Create your models here.
class Like(Date):
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        default = ""
    )
    tweet = models.ForeignKey(
        "tweet.Tweet",
        on_delete= models.CASCADE,
        default = ""
    )

    def __str__(self):
        return f"{self.user}'s like"
