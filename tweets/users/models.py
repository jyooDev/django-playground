from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.
class User(AbstractUser):
    class GenderChoices(models.TextChoices):
        MALE = ("male", "Male")
        FEMALE = ("female", "Female")
    
    username = models.CharField(max_length=150, primary_key=True)
    first_name = models.CharField(max_length=150, editable=False)
    last_name = models.CharField(max_length=150,editable=False)
    name = models.CharField(max_length=150, default="")
    avatar = models.ImageField(blank=True)
    gender = models.CharField(max_length=6, choices=GenderChoices)

    

    def __str__(self):
        return self.username