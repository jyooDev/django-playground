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
        truncated_payload = f"{self.payload[:50]}..." if len(self.payload) >= 50 else self.payload
        return f"{self.user}: {truncated_payload}"


class Like(Date):
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        default = ""
    )
    tweet = models.ForeignKey(
        "tweet.Tweet",
        on_delete= models.CASCADE,
        related_name="likes",
        default = ""
    )

    def __str__(self):
        return f"{self.user}'s like"

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'tweet'], name='unique_like_per_user_per_tweet')
        ]