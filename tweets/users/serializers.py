from rest_framework import serializers
from .models import User

class UserSerializer(serializers.Serializer):
    username = serializers.CharField(
        max_length=150, 
        read_only=True,
    )
    name = serializers.CharField(
        max_length=150, 
        required=True
    )

    email = serializers.CharField()
    gender = serializers.ChoiceField(choices=User.GenderChoices.choices)