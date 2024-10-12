from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.
class User(AbstractUser):
    class GenderChoices(models.TextChoices):
        MALE = ("male", "Male")
        FEMALE = ("female", "Female")
    first_name = models.CharField(max_length=150, editable=False)
    last_name = models.CharField(max_length=150,editable=False)
    name = models.CharField(max_length=150)
    avatar = models.ImageField(blank=True)
    gender = models.CharField(max_length=6, choices=GenderChoices)

    def tweets_ct(self):
        return self.tweets.count()
    
    tweets_ct.short_description = "#tweets"

    def __str__(self):
        return self.username