from rest_framework import serializers
from .models import User

class UserSerializer(serializers.Serializer):
    username = serializers.CharField(
        max_length=150, 
    )
    name = serializers.CharField(
        max_length=150, 
        required=True
    )

    email = serializers.CharField()
    gender = serializers.ChoiceField(choices=User.GenderChoices.choices)

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance  