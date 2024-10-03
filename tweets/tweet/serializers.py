from rest_framework import serializers
from .models import Tweet

class TweetSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    payload=serializers.CharField(
        max_length=180,
        required=True,
    )
    user = serializers.CharField(
        max_length=150,
        read_only=True,
    )
    
    likes_ct = serializers.IntegerField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)