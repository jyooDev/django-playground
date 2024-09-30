from django.db import models
from date.models import Date
# Create your models here.
class Tweet(Date):
    payload = models.CharField(max_length=180)
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="tweets",
        default = ""
    )

    def likes_ct(self):
        return self.likes.count()

    likes_ct.short_description = '#likes'
    
    
    def __str__(self):
        return f"{self.user}'s Tweet"
