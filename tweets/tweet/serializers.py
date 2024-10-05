from rest_framework import serializers
from .models import Tweet

class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ['pk', 'user', 'payload', 'likes_ct', 'created_at', 'updated_at']