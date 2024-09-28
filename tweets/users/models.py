from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.
class User(AbstractUser):
    class GenderChoices(models.TextChoices):
        MALE = ("male", "Male")
        FEMALE = ("female", "Female")
    
    class LanguageChoices(models.TextChoices):
        KR = ("kr", "Korean")
        EN = ("en", "English")

    class CurrencyChoices(models.TextChoices):
        WON = ("won", "Korean Won")
        USE = ("usd", "Dollar")

    username = models.CharField(max_length=150, primary_key=True)
    first_name = models.CharField(max_length=150, editable=False)
    last_name = models.CharField(max_length=150,editable=False)
    name = models.CharField(max_length=150, default="")
    avatar = models.ImageField(blank=True)
    is_host = models.BooleanField("host", default=False)
    gender = models.CharField(max_length=6, choices=GenderChoices)
    language = models.CharField(max_length=2, choices=LanguageChoices)
    currency = models.CharField(max_length=3, choices=CurrencyChoices)

    def __str__(self):
        return self.username